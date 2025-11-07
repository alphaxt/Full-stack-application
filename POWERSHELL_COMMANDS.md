# PowerShell Commands Guide

Since you're using PowerShell on Windows, here are the correct commands:

## Installation Commands

### Option 1: Run commands separately

```powershell
# Install Node.js dependencies
cd dealerships-service
npm install
cd ..

# Install Python dependencies
cd djangoapp
pip install -r requirements.txt
cd ..
```

### Option 2: Use semicolon (;) to chain commands

```powershell
# Install Node.js dependencies
cd dealerships-service; npm install; cd ..

# Install Python dependencies
cd djangoapp; pip install -r requirements.txt; cd ..
```

### Option 3: Use the setup script

```powershell
.\setup.ps1
```

## Running the Application

### Start MongoDB (if not using Docker)
```powershell
# If MongoDB is installed as a service, it should already be running
# Or use Docker:
docker run -d -p 27017:27017 --name mongodb mongo:7
```

### Start Node.js Service
```powershell
cd dealerships-service
npm start
```

### Start Django Application (in a new terminal)
```powershell
cd djangoapp
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## PowerShell vs Bash Differences

| Bash | PowerShell |
|------|------------|
| `&&` | `;` or separate commands |
| `\` | `` ` `` (backtick) for line continuation |
| `export VAR=value` | `$env:VAR="value"` |
| `echo $VAR` | `Write-Host $env:VAR` |

## Common PowerShell Commands

```powershell
# Change directory
cd "path\to\directory"

# List files
Get-ChildItem
# or
ls
# or
dir

# Run multiple commands
cd djangoapp; python manage.py runserver

# Set environment variable
$env:PORT="3000"

# Check if command exists
Get-Command npm
```

## Troubleshooting

### If npm is not found:
```powershell
# Check if Node.js is installed
node --version
npm --version

# If not installed, download from nodejs.org
```

### If pip is not found:
```powershell
# Check if Python is installed
python --version
# or
py --version

# Install pip if needed
python -m ensurepip --upgrade
```

### If you get execution policy errors:
```powershell
# Allow script execution (run as Administrator)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```


