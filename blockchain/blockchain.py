#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Creating a Blockchain

# To be installed: 
# Flask
# Postman HTTP client: https://getpostman.com/

# Importing libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Building a Blockchain

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create(proof = 1, prev_hash = '0')

# Mining the Blockchain



