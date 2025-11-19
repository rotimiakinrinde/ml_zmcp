# Employee Attrition API - Windows Deployment Script
# Run this in PowerShell

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Employee Attrition API - Deployment Script" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

# Check Docker
Write-Host "`nChecking prerequisites..." -ForegroundColor Yellow
if (Get-Command docker -ErrorAction SilentlyContinue) {
    Write-Host "✓ Docker is installed" -ForegroundColor Green
} else {
    Write-Host "✗ Docker is not installed" -ForegroundColor Red
    Write-Host "  Please install Docker Desktop from: https://www.docker.com/products/docker-desktop" -ForegroundColor Yellow
    exit
}

if (Get-Command docker-compose -ErrorAction SilentlyContinue) {
    Write-Host "✓ Docker Compose is installed" -ForegroundColor Green
} else {
    Write-Host "✗ Docker Compose is not installed" -ForegroundColor Red
    exit
}

# Check model files
Write-Host "`nChecking model files..." -ForegroundColor Yellow
$modelFiles = @(
    "models\random_forest_attrition.pkl",
    "models\model_metadata.json",
    "models\feature_names.json"
)

$allFilesExist = $true
foreach ($file in $modelFiles) {
    if (Test-Path $file) {
        $size = (Get-Item $file).Length
        Write-Host "✓ $file found ($([math]::Round($size/1KB, 2)) KB)" -ForegroundColor Green
    } else {
        Write-Host "✗ $file MISSING" -ForegroundColor Red
        $allFilesExist = $false
    }
}

if (-not $allFilesExist) {
    Write-Host "`nPlease make sure all model files are in the models\ folder" -ForegroundColor Yellow
    exit
}

# Build Docker image
Write-Host "`nBuilding Docker image..." -ForegroundColor Yellow
docker-compose build

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Docker image built successfully" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to build Docker image" -ForegroundColor Red
    exit
}

# Start containers
Write-Host "`nStarting containers..." -ForegroundColor Yellow
docker-compose up -d

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Containers started successfully" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to start containers" -ForegroundColor Red
    exit
}

# Wait for API
Write-Host "`nWaiting for API to be ready..." -ForegroundColor Yellow
$maxAttempts = 30
$attempt = 0

while ($attempt -lt $maxAttempts) {
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:5000/health" -UseBasicParsing -ErrorAction SilentlyContinue
        if ($response.StatusCode -eq 200) {
            Write-Host "✓ API is ready!" -ForegroundColor Green
            break
        }
    } catch {
        $attempt++
        if ($attempt -eq $maxAttempts) {
            Write-Host "✗ API failed to start" -ForegroundColor Red
            Write-Host "`nChecking logs..." -ForegroundColor Yellow
            docker-compose logs --tail=50
            exit
        }
        Write-Host "." -NoNewline
        Start-Sleep -Seconds 2
    }
}

# Success message
Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "Deployment Successful! 🎉" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "`n✓ API is running at: http://localhost:5000" -ForegroundColor Green

Write-Host "`nQuick Commands:" -ForegroundColor Yellow
Write-Host "  • View logs:    docker-compose logs -f"
Write-Host "  • Stop API:     docker-compose down"
Write-Host "  • Restart API:  docker-compose restart"
Write-Host "  • Run tests:    python tests\test_api.py"

Write-Host "`nAPI Endpoints:" -ForegroundColor Yellow
Write-Host "  • Health:       GET  http://localhost:5000/health"
Write-Host "  • Model Info:   GET  http://localhost:5000/model/info"
Write-Host "  • Predict:      POST http://localhost:5000/predict"

Write-Host ""
