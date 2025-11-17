# Создать README файл
cat > README.md << 'EOF'
# AI Review Project

Проект для автоматического код-ревью с использованием AI через Ollama.

## 🚀 Быстрый старт

```bash
# Установить Ollama
sudo snap install ollama
ollama serve
ollama pull codellama:7b

# Установить AI Review
python3 -m venv ~/ai-review-venv
source ~/ai-review-venv/bin/activate
pip install xai-review

# Создать конфиг (.ai-review.yaml)
cat > .ai-review.yaml << 'CONFIG'
llm:
  provider: OLLAMA
  meta:
    model: codellama:7b
    max_tokens: 4000
  http_client:
    api_url: http://localhost:11434
vcs:
  provider: GITHUB
  http_client:
    api_url: https://api.github.com
    api_token: "YOUR_TOKEN"
  pipeline:
    owner: "your-username"
    repo: "your-repo"
    pull_number: "PR_NUMBER"
CONFIG

# Запустить ревью
ai-review run