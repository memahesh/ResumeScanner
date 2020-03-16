# views.py

from flask import flash, redirect, render_template, request, session, abort, url_for, jsonify
from functools import wraps
import logging
import json
import re
import nltk

nltk.download('stopwords')
nltk.download('punkt')


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import os
from app import app
# from .models import *

from PyPDF2 import PdfFileReader


@app.route('/filter', methods=['GET'])
def skill_filter():

    # print(request.form)

    path = request.args.get('path')
    query = request.args.get('q')

    print(path, query)

    resume = os.listdir(path)

    filtered_resume = []

    for d in resume:
        tPath = os.path.join(path, d)
        if check(tPath, query.lower()):
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