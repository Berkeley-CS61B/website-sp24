from csv import DictReader
import re
from yaml import load, dump
from google_drive_downloader import GoogleDriveDownloader as gdd
import os.path

"""
The purpose of this script is to generate the 2 .yml files for tas + tutors
to display on the course website. This takes 3 steps:

1. Convert staff responses into a separate spreadsheet with just the following
   information (must be done before invoking this script):

        a. E-mail
        b. Name
        c. Bio
        d. Appointment ('ta' or 'tutor' or 'ai')
        e. Link to photo on google drive (make sure sharing is set to 'Anyone with link')
        f. Pronouns
        g. Link to personal website

2. Download .csv and place in this directory.

3. Invoke this script which will ask for the .csv filename, which then downloads
   all the images to the assets directory and updates the .yml files

4. Invoke the resize.py script in '/assets/staff/'

NOTE: If we keep repeatedly trying, Google Drive will pick up and temporarily
network ban you from accessing the photos, so be aware of that.

@author: onk

"""

IMG_ID_PATTERN = r'((?:\w|-){33})'

long_line = '-' * 50

csv_file_name = "staff.csv"
# print("Now we will ask for the column headers.")
# print(long_line)

email = "Email Address"
name = "Full Name"
bio = "Bio"
appointment = "Appointment"
photo_link = "Photo"
pronouns = "Pronouns"
website_link = "Personal Website"


with open(csv_file_name, newline='') as csvfile:
    reader = DictReader(csvfile)
    for row in reader:
        md = '---\n'
        staff_member = {}
        staff_member['email'] = row[email]
        staff_member['name'] = row[name]
        staff_member['bio'] = row[bio]

        staff_type = row[appointment]
        gdrive_link = row[photo_link]
        _name = staff_member['name']

        staff_member['photo'] = None
        staff_member['pronouns'] = row[pronouns]
        staff_member['link'] = row[website_link] or ''

        md += 'name: ' + _name + '\n'
        md += 'pronouns: ' + staff_member['pronouns'] + '\n'
        md += 'role: ' + staff_type + '\n'
        md += 'email: ' + staff_member['email'] + '\n'
        md += 'website: ' + str(staff_member['link']) + '\n'

        hyphenated_name = _name.lower().replace(' ', '-')
        img_path = f'{hyphenated_name}-1.jpg'

        staff_member['photo'] = img_path
        if os.path.exists(f'{img_path}'):
            continue

        if re.findall(IMG_ID_PATTERN, gdrive_link) == []:
            print(f'Bad link for {_name}, not downloading image: {gdrive_link}')
            continue
        img_id = re.findall(IMG_ID_PATTERN, gdrive_link)[0]

        gdd.download_file_from_google_drive(
            file_id=img_id,
            dest_path=os.path.join(os.getcwd(), os.pardir, 'assets/', 'staff/', img_path),
            overwrite=True,
        )

        print(gdrive_link)

        md += 'photo: ' + img_path + '\n'
        md += '---' + '\n\n'
        md += staff_member['bio'] 
        file_name = hyphenated_name + '.md'
        file_path = os.path.join(os.getcwd(), os.pardir, '_staffers/', file_name)
        with open(file_path, 'w') as file:
            file.write(md)
