Title: html iframe use javascript to add css files
Date: 2011-03-19 19:07
Author: carlcarl
Post_ID: 7
Category: js
Slug: html-iframe-use-javascript-to-add-css-files

 

	:::javascript
	frame.load(function() {
		var frm = frames['frame'].document;
		var otherhead = frm.getElementsByTagName("head")[0];
		var link = frm.createElement("link");
		link.setAttribute("rel", "stylesheet");
		link.setAttribute("type", "text/css");
		link.setAttribute("href", "style.css");
		otherhead.appendChild(link);
	});
