# theme.py

custom_ui_html = """
<!DOCTYPE html>
<html>
<head>
    <title>FᴀsᴛAɴɪᴍᴇAᴘɪ Documentation</title>
    <link rel="stylesheet" type="text/css" href="/custom_ui/custom_ui.css">
</head>
<body>
    <h1>Welcome to FᴀsᴛAɴɪᴍᴇAᴘɪ Documentation</h1>
    <p>Use the API endpoints listed below to interact with FᴀsᴛAɴɪᴍᴇAᴘɪ.</p>

    <h2>API Endpoints</h2>
    <ul>
        <li><a href="/latest">Latest Anime Scrapper</a></li>
        <li><a href="/search">Search Anime</a></li>
        <li><a href="/anime">Anime Information</a></li>
        <li><a href="/episode">Episode Information</a></li>
        <li><a href="/stream">Episode Stream</a></li>
    </ul>
</body>
</html>
"""

custom_ui_css = """
body {
    font-family: Arial, sans-serif;
    padding: 20px;
}

h1 {
    color: #333;
}

p {
    color: #666;
}

h2 {
    color: #555;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    margin-bottom: 10px;
}

a {
    color: #007bff;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
"""
