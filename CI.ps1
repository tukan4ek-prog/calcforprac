Write-Host "=== Загрузка актуального состояния с сервера ==="
git pull origin main

Write-Host "=== Запуск unittest ==="
python -m unittest calctrytest.py -v

Write-Host "=== Установка приложения через setup.exe ==="
Start-Process -FilePath ".\setup.exe" -ArgumentList "/S" -Wait

Write-Host "=== CI успешно завершён ==="