# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

CodeSVG = """
<svg width="210" height="210" xmlns="http://www.w3.org/2000/svg" version="1.1">
    <g>
        <!-- Ethical Value : Social To Organic -->
        <path id="svg_1" fill="#a0a0a0"
            d="M 105,105 L 105,%(y_social)s L %(x_organic)s,105 Z"/>

        <!-- Ethical Value : Organic To Packaging -->
        <path id="svg_2" fill="#a0a0a0"
            d="M 105,105 L %(x_organic)s,105 L 105,%(y_packaging)s Z"/>

        <!-- Ethical Value : Packaging To Local -->
        <path id="svg_3" fill="#a0a0a0"
            d="M 105,105 L 105,%(y_packaging)s L %(x_local)s,105 Z"/>
        <!-- Ethical Value : Local To Social -->
        <path id="svg_4" fill="#a0a0a0"
            d="M 105,105 L %(x_local)s,105 L 105,%(y_social)s Z"/>

        <!-- base -->
        <line id="svg_101" stroke="#919191" fill="none"
            y2="105" x2="30" y1="105" x1="180"/>
        <line id="svg_102" stroke="#919191" fill="none"
            y2="30" x2="105" y1="180" x1="105"/>

        <!-- Level 1 -->
        <line id="svg_11" stroke="#919191" fill="none"
            y2="105" x2="120" y1="90" x1="105"/>
        <line id="svg_12" stroke="#919191" fill="none"
            y2="90" x2="105" y1="105" x1="90"/>
        <line id="svg_13" stroke="#919191" fill="none"
            y2="105" x2="90" y1="120" x1="105"/>
        <line id="svg_14" stroke="#919191" fill="none"
            y2="120" x2="105" y1="105" x1="120"/>

        <!-- Level 2 -->
        <line id="svg_21" stroke="#919191" fill="none"
            y2="105" x2="135" y1="75" x1="105"/>
        <line id="svg_22" stroke="#919191" fill="none"
            y2="75" x2="105" y1="105" x1="75"/>
        <line id="svg_23" stroke="#919191" fill="none"
            y2="105" x2="75" y1="135" x1="105"/>
        <line id="svg_24" stroke="#919191" fill="none"
            y2="135" x2="105" y1="105" x1="135"/>

        <!-- Level 3 -->
        <line id="svg_31" stroke="#919191" fill="none"
            y2="105" x2="150" y1="60" x1="105"/>
        <line id="svg_32" stroke="#919191" fill="none"
            y2="60" x2="105" y1="105" x1="60"/>
        <line id="svg_33" stroke="#919191" fill="none"
            y2="105" x2="60" y1="150" x1="105"/>
        <line id="svg_34" stroke="#919191" fill="none"
            y2="150" x2="105" y1="105" x1="150"/>

        <!-- Level 4 -->
        <line id="svg_41" stroke="#919191" fill="none"
            y2="105" x2="165" y1="45" x1="105"/>
        <line id="svg_42" stroke="#919191" fill="none"
            y2="45" x2="105" y1="105" x1="45"/>
        <line id="svg_43" stroke="#919191" fill="none"
            y2="105" x2="45" y1="165" x1="105"/>
        <line id="svg_44" stroke="#919191" fill="none"
            y2="165" x2="105" y1="105" x1="165"/>

        <!-- Level 5 -->
        <line id="svg_51" stroke="#919191" fill="none"
            y2="105" x2="180" y1="30" x1="105"/>
        <line id="svg_52" stroke="#919191" fill="none"
            y2="30" x2="105" y1="105" x1="30"/>
        <line id="svg_53" stroke="#919191" fill="none"
            y2="105" x2="30" y1="180" x1="105"/>
        <line id="svg_54" stroke="#919191" fill="none"
            y2="180" x2="105" y1="105" x1="180"/>

        <!-- Text -->
        <text id="svg_111"
            text-anchor="middle" font-family="Sans-serif" font-size="15"
            y="110" x="195">%(organic_name)s</text>
        <text id="svg_112"
            text-anchor="middle" font-family="Sans-serif" font-size="15"
            y="25" x="105">%(social_name)s</text>
        <text id="svg_113"
            text-anchor="middle" font-family="Sans-serif" font-size="15"
            y="110" x="18">%(local_name)s</text>
        <text id="svg_114"
            text-anchor="middle" font-family="Sans-serif" font-size="15"
            y="195" x="105">%(packaging_name)s</text>
    </g>
</svg>
"""
