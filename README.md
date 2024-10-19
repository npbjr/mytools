# About
This app will have multiple pages in the future, each pages are tools necessary to help people in their daily work, e.g video converter, video downloader, pdf converter etc.

## Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

## Objectives

To create a video downloader app that can download different videos from social media platforms

## Goals

To handle 100k users.

To make it deployable to different cloud platforms making sure infra config is setup correctly to scale vertically or horizontally.

To make the app user friendly that they will keep using it.

To learn different approach in configuring and deploying apps.

## Setup Instructions

Follow these steps to set up the project:

1. Create a Virtual Environment
   
```bash
git clone https://github.com/npbjr/mytools.git
```
cd mytools


2. Create a Virtual Environment
Create a virtual environment using venv:

```bash
python -m venv venv
```
3. Activate the Virtual Environment
On Windows:

```bash
venv\Scripts\activate
```
On macOS/Linux:

```bash
source venv/bin/activate
```
4. Install Dependencies

```bash
pip install -r requirements.txt
```
5. run the app

```bash
python flask_app.py
```
The application should now be running on http://127.0.0.1:5000/.
sample live app https://npbjr.pythonanywhere.com/


if you want to test in docker environment
```bash
docker-compose up --build
```
then run in browser http://localhost

you can also test running in gunicorn
```bash
gunicorn -k eventlet -w 1 flask_app:app
```
then run in browser http://127.0.0.1:8000



