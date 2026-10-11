$ErrorActionPreference = "Stop"

Write-Host "Запуск Ollama..."
docker compose up -d

Write-Host "Ожидание запуска API Ollama..."

$ready = $false

for ($i = 0; $i -lt 60; $i++) {
    try {
        Invoke-RestMethod `
            -Uri "http://localhost:11434/api/tags" `
            -ErrorAction Stop | Out-Null

        $ready = $true
        break
    }
    catch {
        Start-Sleep -Seconds 2
    }
}

if (-not $ready) {
    throw "API Ollama недоступен"
}

Write-Host "Загрузка модели llama3..."
docker compose exec -T ollama ollama pull llama3

Write-Host "Ollama запущена, модель llama3 готова к работе!"