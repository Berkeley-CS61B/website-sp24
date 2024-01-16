---
layout: page
title: >-
  Linux/Unix
parent: >-
  Lab 01: Setup
grand_parent: Labs
has_toc: false
has_right_toc: true
released: true
---

## A. Setup

Setting up Linux for 61B is super easy, all you have to do is use your package
manager (apt, yum, etc) to install the Java JDK, git and curl.

To install and configure the Java JDK, git and curl on Ubuntu:

```sh
sudo apt install openjdk-17-jdk git curl
```

If you're able to successfully install Java, you can skip the step later on in the lab to 
download it through IntelliJ ([Installing Java](index.md#installing-intellij)).

You can also install IntelliJ using: 
```shell
sudo snap install intellij-idea-community --classic
```

If IntelliJ installs successfully without errors using this command, skip over the installing IntelliJ section 
in the main lab page. 
