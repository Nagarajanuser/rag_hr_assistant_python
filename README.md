
Step: 1
    python -m venv venv

if above one fail, First delete "venv" folder after use below command
    python -m pip install --upgrade pip setuptools wheel
after again use this below command
    python -m venv venv

Step: 2
venv\Scripts\activate

Step: 3
pip install -r requirements.txt

-----------------------------------------------------------------------------
Required packages
-----------------------------------------------------------------------------
# Initial Required
pip install pypdf
pip install dotenv

# to embedd
pip install sentence-transformers

# Upload the chunk to Vector database (pinecone)
pip install pinecone

# to get final aswer use LLM (user query + chunk data) 
pip install google-genai


-----------------------------------------------------------------------------
Use this APP
-----------------------------------------------------------------------------
To upload Documents
    python upload_documents.py

Based on user query get the Rasponse
    python user_query.py

