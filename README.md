# Agentic play

## N8N

- N8N need to have the following community package installed after setup: `n8n-nodes-mcp`
- PostgreSQl db needs vector externsion enabled - should move to a appropriate docker image in future (`pgvector/pgvector:latest`)

### To install vector extension
Something like this on the postgre instance:

```bash
apk add --no-cache make build-base &&
cd /tmp &&
rm -rf pgvector-0.8.0 v0.8.0.tar.gz &&
wget https://github.com/pgvector/pgvector/archive/refs/tags/v0.8.0.tar.gz &&
tar -xzf v0.8.0.tar.gz &&
cd pgvector-0.8.0 &&
$(make || true) &&
$(make install || true) &&
cp *.so $(pg_config --pkglibdir)/ &&
cp sql/vector*.sql $(pg_config --sharedir)/extension/ &&
cp vector.control $(pg_config --sharedir)/extension/
```

### To run

```bash
docker-compose up -d
```

## Google ADK

Look into using uv as a package manager, poetry felt painful.

### Start from scratch

```bash
brew install python pyenv
echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
cd ~/Sites/agentic-play
pyenv install 3.10.14
python -m venv venv
source venv/bin/activate
pyenv global 3.10.14
pyenv local 3.10.14
python --version
pip install -r requirements.txt
crawl4ai-setup
```

#### Setup first agent
```bash
mkdir -p multi_tool_agent
echo "from . import agent" > multi_tool_agent/__init__.py
touch multi_tool_agent/agent.py
touch multi_tool_agent/.env
echo "GOOGLE_GENAI_USE_VERTEXAI=FALSE" >> multi_tool_agent/.env
echo "GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE" >> multi_tool_agent/.env
```

### Start from current

```bash
python3 -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
crawl4ai-setup
```

### Run the dev UI

```bash
adk web
```
