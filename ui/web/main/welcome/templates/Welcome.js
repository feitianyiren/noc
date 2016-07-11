!function(){var e=Handlebars.template,o=NOC.templates.main_welcome=NOC.templates.main_welcome||{};o.Welcome=e({compiler:[7,">= 4.0.0"],main:function(e,o,t,n,a){return'<style>\n.welcome_title {\n    font-size: 18px;\n    font-weight: bold;\n    padding: 4px 4px 4px 8px;\n}\n\n.welcome_body {\n    padding: 4px 4px 4px 8px;\n    font-size: 14px;\n}\n\n.welcome_body a:visited, .welcome_body a {\n    color: black;\n    text-decoration: none;\n}\n\n.welcome_body a:hover {\n    color: #808080;\n    text-decoration: underline;\n}\n\n#welcome-logo {\n    border: none;\n    float: left;\n    margin: 4px;\n}\n\n.welcome_body h2 {\n    font-size: 10pt;\n}\n</style>\n<div class="welcome_title">Welcome to the NOC Project!</div>\n<div class="welcome_body">\n<img id="welcome-logo" src="/static/img/logo_black.svg" width="32" height="32"/>\n<a href="http://nocproject.org">NOC</a> is an Operation Support System (OSS)\nfor telecom companies, service providers, and enterprise Network Operation Centers\n(<a href="http://en.wikipedia.org/wiki/Network_operations_center">NOC</a>).<br/>\nNOC is open source and released under the terms of <a href="http://kb.nocproject.org/display/SITE/License">BSD LICENSE</a>.\nRead <a href="http://kb.nocproject.org/display/SITE/About">more...</a><br/><br/>\n\n<h2>Getting started:</h2>\n<i class="fa fa-hand-o-right"></i> <a href="http://kb.nocproject.org/display/SITE/Registration">Join the Project</a><br/>\n<i class="fa fa-desktop"></i> <a href="http://nocproject.org/">Official site</a><br/>\n<i class="fa fa-book"></i> <a href="http://kb.nocproject.org/display/DOC/Home">Online documentation</a><br/>\n<i class="fa fa-question-circle"></i> <a href="http://kb.nocproject.org/questions">Ask questions</a><br/>\n<i class="fa fa-question-circle"></i> <a href="http://kb.nocproject.org/display/FAQ/Home">FAQ</a><br/>\n<i class="fa fa-bug"></i> <a href="http://bt.nocproject.org/">Issue Tracker</a><br/>\n\n<h2>Follow us:</h2>\n    <i class="fa fa-bullhorn"></i> <a href="http://static.nocproject.org/irclog/">#nocproject.org at irc.freenode.net</a><br/>\n    <i class="fa fa-linkedin"></i> <a href=http://www.linkedin.com/company/nocproject-org?trk=fc_badge">LinkedIn</a><br/>\n    <i class="fa fa-twitter"></i> <a href="http://www.twitter.com/nocproject_org">Twitter</a><br/>\n    <i class="fa fa-bitbucket"></i> <a href="https://bitbucket.org/nocproject/noc">Bitbucket</a><br/>\n    <i class="fa fa-youtube"></i> <a href="http://www.youtube.com/user/thenocproject">YouTube</a><br/>\n    <i class="fa fa-info-circle"></i> <a href="http://www.openhub.net/p/noc/">Open Hub</a>\n</div>\n'},useData:!0})}();Ext.define("NOC.main.welcome.templates.Welcome", {});