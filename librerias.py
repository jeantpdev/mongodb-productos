from flask import Flask, request, jsonify, Blueprint
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
import cloudinary
import cloudinary.uploader
import os
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from functools import wraps
from dotenv import load_dotenv
load_dotenv()
