# Ez-Query
## SQL Query Generator Powered by ChatGPT

Ez_query allows you to generate sql queries using ChatGPT with the added benefit of retrieving your table schemas for you. 

ChatGPT is capable of helping you write SQL queries but only if you provide it your table schemas first. This would mean you have to retrieve them youself manually and enter them into ChatGPT. Doing this multiple times is tedious and time-consuming. 

Ez_query makes the process of retrieving your table schemas extremely simple and allows you to do this all in the terminal.

## Installation


```sh
pip install ez_query
```
## Usage

```sh
ez_query -h
ez_query --openai_api_key sk-fake-key --db_host=localhost --db_user=root --db_pass=root --db_name=employees
```
