Following tutorial https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH

## Using python in Html
a code block is created with the following syntax: 
    {% block body %}
        <\code here>
    {% endblock %}

## configuring app
To add to the configuration of an app use: 
```
app.config
```

## Helpful for server
If the server won't reset use this bash cmd to reset it
```
kill -9 $(ps -A | grep python | awk '{print $1}') 
```
If styling wont update use this to reset cahche in browser
```
ctrl+shift+r 
```
