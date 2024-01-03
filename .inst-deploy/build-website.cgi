#!/usr/bin/env python3
# vim: set ft=python ts=4 sw=4 et:

from pathlib import Path
import hashlib
import hmac
import json
import os
import subprocess
import sys
import urllib

BUILD_SCRIPT_PATH = Path("~/web-repos/deploy.sh").expanduser()
DEBUG = False
MAIN_REF = "refs/heads/main"
SECRET_FILE_PATH = Path("~/web-repos/secret.txt").expanduser()

def reply(status, msg="", content_type="text/plain"):
    print(f"Status: {status}\nContent-Type: {content_type}")
    print("")
    print(msg)

def validate_body():
    try:
        if (SECRET_FILE_PATH.stat().st_mode & 0o077) != 0:
            SECRET_FILE_PATH.chmod(0o600)

        sig_alg, expected_sig = os.getenv("HTTP_X_HUB_SIGNATURE", "=").split("=")
        if sig_alg != "sha1":
            reply(400, "Unsupported signature")
            sys.exit(0)

        body = sys.stdin.read()
        secret = SECRET_FILE_PATH.read_text(encoding="utf-8").strip()
        actual_sig = hmac.new(secret.encode("utf-8"), msg=body.encode("utf-8"), digestmod=hashlib.sha1).hexdigest()
        if not hmac.compare_digest(actual_sig, expected_sig):
            raise Exception("Signature mismatch")
        return json.loads(body)
    except:
        if DEBUG:
            import traceback
            reply(401, traceback.format_exc())
        else:
            reply(401)
        sys.exit(0)

try:
    body = validate_body()
    semester = "su87"
    try:
        qs = urllib.parse.parse_qs(os.getenv("QUERY_STRING", ""))
        if "semester" in qs: semester = qs["semester"][0]
    except:
        if DEBUG:
            import traceback
            reply(400, traceback.format_exc())
        else:
            reply(400, "Invalid query string")
        sys.exit(0)
    event = os.getenv("HTTP_X_GITHUB_EVENT", "")
    if event == "ping":
        reply(200, "pong")
    elif event == "push":
        ref = body.get("ref")
        if ref == MAIN_REF:
            commit = body.get("after")
            output = subprocess.check_output([BUILD_SCRIPT_PATH, semester, commit], stderr=subprocess.STDOUT)
            reply(200, "build=true")
            print(f"commit={commit}")
            print(f"ref={ref}")
            print(f"semester={semester}")
            print(output.decode("utf-8"))
        else:
            reply(200, "build=false")
            print(f"ref={ref}")
            print(f"semester={semester}")
    else:
        reply(400, "Unsupported event")
        sys.exit(0)
except SystemExit:
    pass
except subprocess.CalledProcessError as e:
    if DEBUG:
        import traceback
        reply(500, traceback.format_exc())
        print(e.output.decode("utf-8"))
    else:
        reply(500)
    sys.exit(0)
except:
    if DEBUG:
        import traceback
        reply(500, traceback.format_exc())
    else:
        reply(500)
    sys.exit(0)
