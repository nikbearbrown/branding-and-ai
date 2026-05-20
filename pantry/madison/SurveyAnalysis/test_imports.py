# Test script to verify all libraries are installed correctly

print("Testing library imports...")
print("-" * 50)

try:
 import pandas as pd
 print(" pandas imported successfully")
except ImportError as e:
 print(f" pandas failed: {e}")

try:
 import numpy as np
 print(" numpy imported successfully")
except ImportError as e:
 print(f" numpy failed: {e}")

try:
 import openai
 print(" openai imported successfully")
except ImportError as e:
 print(f" openai failed: {e}")

try:
 import plotly
 print(" plotly imported successfully")
except ImportError as e:
 print(f" plotly failed: {e}")

try:
 import matplotlib
 print(" matplotlib imported successfully")
except ImportError as e:
 print(f" matplotlib failed: {e}")

try:
 import streamlit as st
 print(" streamlit imported successfully")
except ImportError as e:
 print(f" streamlit failed: {e}")

try:
 from dotenv import load_dotenv
 print(" python-dotenv imported successfully")
except ImportError as e:
 print(f" python-dotenv failed: {e}")

try:
 import sklearn
 print(" scikit-learn imported successfully")
except ImportError as e:
 print(f" scikit-learn failed: {e}")

print("-" * 50)
print(" All libraries imported successfully!")
print(" You're ready to start building!")