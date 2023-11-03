### ProAlgoTrader

This is a default template for your strategy.

## Step 1

Clone strategy

```bash
git clone <PROJECT_REPOSITORY_URL> <PROJECT_DIRECTORY>
```

You can find your PROJECT_REPOSITORY_URL from ProAlgoTrader Project Dashboard.

## Step 2

Create a virtual environment

```bash
cd <PROJECT_DIRECTORY>

python -m venv .venv
```

## Step 3

Install required packages

```bash
pip install -r requirements.txt
```

## Step 4

Run strategy

```bash
trader_cli run <PROJECT_ID> <MODE>

MODE can be Paper or Live.
```

## Step 5

Available `trader_cli` commands

```bash
trader_cli login
trader_cli run <PROJECT_ID> <MODE>
trader_cli deploy <PROJECT_ID> <MODE>
```
