from flask import Flask, request, jsonify, Blueprint
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv
load_dotenv()
