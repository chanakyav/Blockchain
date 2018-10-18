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
        
    def create_block(self, proof, prev_hash):
        block = {'index': len(self.chain)+1,
                 'timestamp': str(datetime.date.now()),
                 'proof': proof,
                 'prev_hash': prev_hash}
        
        self.chain.append(block)
        return block

# Mining the Blockchain



