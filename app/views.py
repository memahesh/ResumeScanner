# views.py

from flask import flash, redirect, render_template, request, session, abort, url_for, jsonify
from functools import wraps
import logging
import json
import re
import nltk

nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import os
from app import app
# from .models import *

from PyPDF2 import PdfFileReader

RESUME_DIR = 'app/static/resume/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/filter', methods=['POST'])
def skill_filter():

    # print(request.form)

    query = request.form.get('q')

    resume = os.listdir(RESUME_DIR)

    filtered_resume = []

    for d in resume:
        path = RESUME_DIR+d
        if check(path, query.lower()):
            filtered_resume.append(d)

    return jsonify({
        'resume': filtered_resume,
    })


def text_preprocessing(text):

    text = text.lower()
    # Tokenizing the text
    tokens = word_tokenize(text)
    # Filtering out punctuation
    words = [word for word in tokens if word.isalpha()]

    stop_words = set(stopwords.words('english'))

    words = [w for w in words if not w in stop_words]

    return words


def check(path, query):

    text = ""

    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        i = 0
        for page in range(pdf.getNumPages()):
            page = pdf.getPage(i)
            text = text + " " + page.extractText()
            i+=1
    
    tokens = text_preprocessing(text)

    for t in tokens:
        if query in t:
            return True

    return False