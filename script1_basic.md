# Gist

* Request object specifies the URL you want to fetch.
    * Request -- An object that encapsulates the state of a request.  The
      state can be as simple as the URL.  It can also include extra HTTP
      headers, e.g. a User-Agent.
* Calling urlopen with this Request object returns a response object for the URL requested.
* The number of HTTP methods you'll use is quite small—there are just four HTTP "verbs" you'll need to know! They are:

GET: retrieves information from the specified source.
POST: sends new information to the specified source.
PUT: updates existing information of the specified source.
DELETE: removes existing information from the specified source.
* The requests library only deals with HTTP, HTTPS while in the urllib2 urlopen can also open others like file./// etc

## Anatomy of a Request

* An HTTP request is made up of three parts:

    * The request line, which tells the server what kind of request is being sent (GET, POST, etc.) and what resource it's looking for;
    * The header, which sends the server additional information (such as which client is making the request)
    * The body, which can be empty (as in a GET request) or contain data (if you're POSTing or PUTing information, that information is contained here).

## Endpoints
* Endpoints are API-defined locations where particular data are stored. Just as you'll GET a pair of pants from PantsWorld or you'll GET a bag of peanuts from PeanutHut, you'll GET something different depending on the endpoint you use.
For instance, if you're using the API for a video hosting service, there might be endpoints for the most popular videos, the most recent videos, or videos belonging to a certain genre or category.

## Authentication & API Keys

* Many APIs require an API key. Just as a real-world key allows you to access something, an API key grants you access to a particular API. Moreover, an API key identifies you to the API, which helps the API provider keep track of how their service is used and prevent unauthorized or malicious activity.

    * Some APIs require authentication using a protocol called OAuth. We won't get into the details, but if you've ever been redirected to a page asking for permission to link an application with your account, you've probably used OAuth.

## HTTP Status Codes
* A successful request to the server results in a response, which is the message the server sends back to you, the client.

The response from the server will contain a three-digit status code. These codes can start with a 1, 2, 3, 4, or 5, and each set of codes means something different. (You can read the full list here). They work like this:

    * 1xx: You won't see these a lot. The server is saying, "Got it! I'm working on your request."

    * 2xx: These mean "okay!" The server sends these when it's successfully responding to your request.

    * 3xx: These mean "I can do what you want, but I have to do something else first." You might see this if a website has changed addresses and you're using the old one; the server might have to reroute the request before it can get you the resource you asked for.

    * 4xx: These mean you probably made a mistake. The most famous is "404," meaning "file not found": you asked for a resource or web page that doesn't exist.

    * 5xx: These mean the server goofed up and can't successfully respond to your request.

## Anatomy of a Response

* The HTTP response structure mirrors that of the HTTP request. It contains:

    * A response line (line 2), which includes the three-digit HTTP status code;

    * A header line or lines (line 3), which include further information about the server and its response;

    * The body (line 5 and line 6), which contains the text message of the response (for example, "404" would have "file not found" in its body).

## Parsing XML
XML (which stands for eXtensible Markup Language) is very similar to HTML—it uses tags between
 angle brackets. The difference is that XML allows you to use tags that you make up, rather than
  tags that the W3C decided on.

## Parsing JSON
JSON (which stands for JavaScript Object Notation) is an alternative to XML.
 It gets its name from the fact that it's data format resembles JavaScript objects, and it is often more succinct than the equivalent XML.