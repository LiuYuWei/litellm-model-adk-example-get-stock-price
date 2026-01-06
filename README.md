# Stock Price Agent (Taiwan Stocks)

This project implements an AI agent using the `google-adk` framework. The agent can provide real-time stock prices for Taiwan stocks using Yahoo Finance.

## Description

The core of this project is the `stock_agent`, which is equipped with a tool to fetch stock prices:

1.  **`get_stock_price(stock_code)`**: Retrieves the current stock price for a given Taiwan stock code (e.g., `2330`). It uses the `yfinance` library to fetch data from Yahoo Finance.

This agent is built using `litellm` to connect to a language model and interprets user requests to call the `get_stock_price` tool.

## Installation

1.  **Set up the Python virtual environment:**
    ```bash
    make setup
    ```

2.  **Install the required dependencies:**
    ```bash
    make install
    ```

3.  **Add .env into adk_agent folder**
    ```
    LITELLM_MODEL_API_KEY=
    LITELLM_MODEL_API_BASE=
    LITELLM_MODEL_MODEL_NAME=openai/
    ```

## Usage

To start the agent server, run the following command:

```bash
make run
```

This will launch the ADK web interface, where you can interact with the agent.

## Agent Details

-   **Name**: `stock_agent`
-   **Description**: An agent designed to answer questions about the stock price.
-   **Instructions**: The agent is instructed to be a helpful assistant that can check stock prices. It identifies the 4-digit stock code from user input and calls the `get_stock_price` tool.

### Tools

-   `get_stock_price(stock_code: str) -> str`

## Dependencies

-   `google-adk`
-   `python-dotenv`
-   `litellm`
-   `yfinance`