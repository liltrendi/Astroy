#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from platform import python_version as version

if int(version()[0]) < 3:
	import sys
	sys.exit("\n\033[0;91mPlease use Python 3 to run this file!\033[0m\n")

try:
	import os
	from progress.bar import IncrementalBar as Bar
	from prettytable import PrettyTable as pt
	from subprocess import call as run
	from time import sleep as wait
	from sys import exit as bye
	from sys import argv as argv
	from urllib.request import urlopen as visit
	from crayons import red,yellow,green,blue,cyan,magenta
except:
	import sys
	sys.exit("\n\033[0;91mInstall the requirements by running 'pip install -r requirements.txt' and then run this using Python 3\033[0m\n")

t=pt()

#default ports
port1=80
port2=555
port3=777
port4=999

banner="""
			    _        _
			   / \   ___| |_ _ __ ___  _   _
			  / _ \ / __| __| '__/ _ \| | | |
			 / ___ \\ __ \ |_| | | (_) | |_| |
			/_/   \_\___/\__|_|  \___/ \__, |
			                           |___/
"""

B="\033[0;96m"
Y="\033[0;93m"
G="\033[0;92m"
P="\033[0;95m"
N="\033[0;39m"
R="\033[0;91m"
C="\033[0;36m"
BR="\033[1m"

html1='''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml"><head><!--[if gte mso 9]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]--><meta content="text/html; charset=utf-8" http-equiv="Content-Type"/><meta content="width=device-width" name="viewport"/><!--[if !mso]><!--><meta content="IE=edge" http-equiv="X-UA-Compatible"/><!--<![endif]--><title></title><!--[if !mso]><!--><link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css"/><!--<![endif]--><style type="text/css">body {margin: 0;padding: 0;}table,td,tr {vertical-align: top;border-collapse: collapse;}* {line-height: inherit;}a[x-apple-data-detectors=true] {color: inherit !important;text-decoration: none !important;}.ie-browser table {table-layout: fixed;}[owa] .img-container div,[owa] .img-container button {display: block !important;}[owa] .fullwidth button {width: 100% !important;}[owa] .block-grid .col {display: table-cell;float: none !important;vertical-align: top;}.ie-browser .block-grid,.ie-browser .num12,[owa] .num12,[owa] .block-grid {width: 675px !important;}.ie-browser .mixed-two-up .num4,[owa] .mixed-two-up .num4 {width: 224px !important;}.ie-browser .mixed-two-up .num8,[owa] .mixed-two-up .num8 {width: 448px !important;}.ie-browser .block-grid.two-up .col,[owa] .block-grid.two-up .col {width: 336px !important;}.ie-browser .block-grid.three-up .col,[owa] .block-grid.three-up .col {width: 336px !important;}.ie-browser .block-grid.four-up .col [owa] .block-grid.four-up .col {width: 168px !important;}.ie-browser .block-grid.five-up .col [owa] .block-grid.five-up .col {width: 135px !important;}.ie-browser .block-grid.six-up .col,[owa] .block-grid.six-up .col {width: 112px !important;}.ie-browser .block-grid.seven-up .col,[owa] .block-grid.seven-up .col {width: 96px !important;}.ie-browser .block-grid.eight-up .col,[owa] .block-grid.eight-up .col {width: 84px !important;}.ie-browser .block-grid.nine-up .col,[owa] .block-grid.nine-up .col {width: 75px !important;}.ie-browser .block-grid.ten-up .col,[owa] .block-grid.ten-up .col {width: 60px !important;}.ie-browser .block-grid.eleven-up .col,[owa] .block-grid.eleven-up .col {width: 54px !important;}.ie-browser .block-grid.twelve-up .col,[owa] .block-grid.twelve-up .col {width: 50px !important;}</style><style id="media-query" type="text/css">@media only screen and (min-width: 695px) {.block-grid {width: 675px !important;}.block-grid .col {vertical-align: top;}.block-grid .col.num12 {width: 675px !important;}.block-grid.mixed-two-up .col.num3 {width: 168px !important;}.block-grid.mixed-two-up .col.num4 {width: 224px !important;}.block-grid.mixed-two-up .col.num8 {width: 448px !important;}.block-grid.mixed-two-up .col.num9 {width: 504px !important;}.block-grid.two-up .col {width: 337px !important;}.block-grid.three-up .col {width: 225px !important;}.block-grid.four-up .col {width: 168px !important;}.block-grid.five-up .col {width: 135px !important;}.block-grid.six-up .col {width: 112px !important;}.block-grid.seven-up .col {width: 96px !important;}.block-grid.eight-up .col {width: 84px !important;}.block-grid.nine-up .col {width: 75px !important;}.block-grid.ten-up .col {width: 67px !important;}.block-grid.eleven-up .col {width: 61px !important;}.block-grid.twelve-up .col {width: 56px !important;}}@media (max-width: 695px) {.block-grid,.col {min-width: 320px !important;max-width: 100% !important;display: block !important;}.block-grid {width: 100% !important;}.col {width: 100% !important;}.col>div {margin: 0 auto;}img.fullwidth,img.fullwidthOnMobile {max-width: 100% !important;}.no-stack .col {min-width: 0 !important;display: table-cell !important;}.no-stack.two-up .col {width: 50% !important;}.no-stack .col.num4 {width: 33% !important;}.no-stack .col.num8 {width: 66% !important;}.no-stack .col.num4 {width: 33% !important;}.no-stack .col.num3 {width: 25% !important;}.no-stack .col.num6 {width: 50% !important;}.no-stack .col.num9 {width: 75% !important;}.video-block {max-width: none !important;}.mobile_hide {min-height: 0px;max-height: 0px;max-width: 0px;display: none;overflow: hidden;font-size: 0px;}.desktop_hide {display: block !important;max-height: none !important;}}</style></head><body class="clean-body" style="margin: 0; padding: 0; -webkit-text-size-adjust: 100%; background-color: #FFFFFF;"><!--[if IE]><div class="ie-browser"><![endif]--><table bgcolor="#FFFFFF" cellpadding="0" cellspacing="0" class="nl-container" role="presentation" style="table-layout: fixed; vertical-align: top; min-width: 320px; Margin: 0 auto; border-spacing: 0; border-collapse: collapse; background-color: #FFFFFF; width: 100%;" valign="top" width="100%"><tbody><tr style="vertical-align: top;" valign="top"><td style="word-break: break-word; vertical-align: top; border-collapse: collapse;" valign="top"><!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color:#FFFFFF"><![endif]--><div style="background-color:#543098;"><div class="block-grid two-up" data-body-width-father="675px" rel="col-num-container-box-father" style="Margin: 0 auto; min-width: 320px; max-width: 675px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: transparent;"><div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;"><!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#543098;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:675px"><tr class="layout-full-width" style="background-color:transparent"><![endif]--><!--[if (mso)|(IE)]><td align="center" width="337" style="background-color:transparent;width:337px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:30px; padding-bottom:0px;"><![endif]--><div class="col num6" data-body-width-son="337" rel="col-num-container-box-son" style="min-width: 320px; max-width: 337px; display: table-cell; vertical-align: top;"><div style="width:100% !important;"><!--[if (!mso)&(!IE)]><!--><div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:30px; padding-bottom:0px; padding-right: 0px; padding-left: 0px;"><!--<![endif]--><div align="center" class="img-container center fixedwidth" style="padding-right: 15px;padding-left: 15px;"><!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 15px;padding-left: 15px;" align="center"><![endif]--><div style="font-size:1px;line-height:5px"> </div><a href="javascript:void(0)" target="_blank"> <img align="center" border="0" class="center fixedwidth" src="https://i.postimg.cc/7bVB2hRV/unnamed-1.png" style="outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; clear: both; height: auto; float: none; border: none; width: 100%; max-width: 67px; display: block;" title="Image" width="67"/></a><!--[if mso]></td></tr></table><![endif]--></div><div class="mobile_hide"><table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%"><tbody><tr style="vertical-align: top;" valign="top"><td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; border-collapse: collapse;" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" height="20" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; width: 100%; border-top: 0px solid transparent; height: 20px;" valign="top" width="100%"><tbody><tr style="vertical-align: top;" valign="top"><td height="20" style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; border-collapse: collapse;" valign="top"><span></span></td></tr></tbody></table></td></tr></tbody></table></div><!--[if (!mso)&(!IE)]><!--></div><!--<![endif]--></div></div><!--[if (mso)|(IE)]></td></tr></table><![endif]--><!--[if (mso)|(IE)]></td><td align="center" width="337" style="background-color:transparent;width:337px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:30px; padding-bottom:20px;"><![endif]--><div class="col num6" data-body-width-son="337" rel="col-num-container-box-son" style="min-width: 320px; max-width: 337px; display: table-cell; vertical-align: top;"><div style="width:100% !important;"><!--[if (!mso)&(!IE)]><!--><div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:30px; padding-bottom:20px; padding-right: 0px; padding-left: 0px;"><!--<![endif]--><div class="mobile_hide"><table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%"><tbody><tr style="vertical-align: top;" valign="top"><td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; border-collapse: collapse;" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" height="32" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; width: 100%; border-top: 0px solid transparent; height: 32px;" valign="top" width="100%"><tbody><tr style="vertical-align: top;" valign="top"><td height="32" style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; border-collapse: collapse;" valign="top"><span></span></td></tr></tbody></table></td></tr></tbody></table></div><div class="mobile_hide"><!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 0px; padding-bottom: 15px; font-family: 'Trebuchet MS', Tahoma, sans-serif"><![endif]--><div style="color:#FFFFFF;font-family:'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif;line-height:150%;padding-top:0px;padding-right:10px;padding-bottom:15px;padding-left:10px;"><div style="font-family: 'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif; font-size: 12px; line-height: 18px; color: #FFFFFF;"><div style="line-height: 18px; font-size: 12px; text-align: center;"><span style="font-size: 18px; line-height: 27px;"><strong><span style="line-height: 27px; font-size: 18px;">Install, Use, Earn.</span></strong></span></div></div></div><!--[if mso]></td></tr></table><![endif]--></div><!--[if (!mso)&(!IE)]><!--></div><!--<![endif]--></div></div><!--[if (mso)|(IE)]></td></tr></table><![endif]--><!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]--></div></div></div><div style="background-image:url('https://postimg.cc/YvP54R9Y');background-position:top center;background-repeat:no-repeat;background-color:#57429C;"><div class="block-grid" data-body-width-father="675px" rel="col-num-container-box-father" style="Margin: 0 auto; min-width: 320px; max-width: 675px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: transparent;"><div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;"><!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-image:url('https://i.postimg.cc/YvP54R9Y/bg-blue-violet-1.png');background-position:top center;background-repeat:no-repeat;background-color:#57429C;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:675px"><tr class="layout-full-width" style="background-color:transparent"><![endif]--><!--[if (mso)|(IE)]><td align="center" width="675" style="background-color:transparent;width:675px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:0px; padding-bottom:50px;"><![endif]--><div class="col num12" data-body-width-son="675" rel="col-num-container-box-son" style="min-width: 320px; max-width: 675px; display: table-cell; vertical-align: top;"><div style="width:100% !important;"><!--[if (!mso)&(!IE)]><!--><div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:0px; padding-bottom:50px; padding-right: 0px; padding-left: 0px;"><!--<![endif]--><table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%"><tbody><tr style="vertical-align: top;" valign="top"><td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; border-collapse: collapse;" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" height="0" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; width: 100%; border-top: 10px solid transparent; height: 0px;" valign="top" width="100%"><tbody><tr style="vertical-align: top;" valign="top"><td height="0" style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; border-collapse: collapse;" valign="top"><span></span></td></tr></tbody></table></td></tr></tbody></table><!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top: 30px; padding-bottom: 0px; font-family: 'Trebuchet MS', Tahoma, sans-serif"><![endif]--><div style="color:#ffffff;font-family:'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif;line-height:120%;padding-top:30px;padding-right:0px;padding-bottom:0px;padding-left:0px;"><div style="line-height: 14px; font-family: 'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif; font-size: 12px; color: #ffffff;"><p style="line-height: 33px; text-align: center; font-size: 12px; margin: 0;"><span style="font-size: 20px;">INTRODUCING</span><strong><span style="font-size: 28px; line-height: 33px;"><br/></span><span style="font-size: 40px; line-height: 96px;">ASTROY</span></strong></p></div></div><!--[if mso]></td></tr></table><![endif]--><table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%"><tbody><tr style="vertical-align: top;" valign="top"><td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; border-collapse: collapse;" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" height="0" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; width: 100%; border-top: 10px solid transparent; height: 0px;" valign="top" width="100%"><tbody><tr style="vertical-align: top;" valign="top"><td height="0" style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; border-collapse: collapse;" valign="top"><span></span></td></tr></tbody></table></td></tr></tbody></table><div align="center" class="img-container center fixedwidth" style="padding-right: 20px;padding-left: 20px;"><!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 20px;padding-left: 20px;" align="center"><![endif]--><div style="font-size:1px;line-height:20px"> </div><a href="javascript:void(0)" target="_blank"> <img align="center" border="0" class="center fixedwidth" src="https://i.postimg.cc/2qJK6S0w/rocket-color.png" style="outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; clear: both; height: auto; float: none; border: none; width: 30%; max-width: 371px; display: block;" title="rocket" width="371"/></a><div style="font-size:1px;line-height:20px"> </div><!--[if mso]></td></tr></table><![endif]--></div><!--[if (!mso)&(!IE)]><!--></div><!--<![endif]--></div></div><!--[if (mso)|(IE)]></td></tr></table><![endif]--><!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]--></div></div></div><div style="background-color:#F4F4FF;"><div class="block-grid" data-body-width-father="675px" rel="col-num-container-box-father" style="Margin: 0 auto; min-width: 320px; max-width: 675px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: transparent;"><div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;"><!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#F4F4FF;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:675px"><tr class="layout-full-width" style="background-color:transparent"><![endif]--><!--[if (mso)|(IE)]><td align="center" width="675" style="background-color:transparent;width:675px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:30px; padding-bottom:30px;"><![endif]--><div class="col num12" data-body-width-son="675" rel="col-num-container-box-son" style="min-width: 320px; max-width: 675px; display: table-cell; vertical-align: top;"><div style="width:100% !important;"><!--[if (!mso)&(!IE)]><!--><div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:30px; padding-bottom:30px; padding-right: 0px; padding-left: 0px;"><!--<![endif]--><!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 35px; padding-bottom: 10px; font-family: 'Trebuchet MS', Tahoma, sans-serif"><![endif]--><div style="color:#CF66FF;font-family:'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif;line-height:120%;padding-top:35px;padding-right:10px;padding-bottom:10px;padding-left:10px;"><div style="font-family: 'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif; font-size: 12px; line-height: 14px; color: #CF66FF;"><p style="font-size: 18px; line-height: 40px; text-align: center; margin: 0;"><span style="font-size: 34px;">Get <strong>paid</strong> to test <br/><strong>mobile applications</strong></span></p></div></div><!--[if mso]></td></tr></table><![endif]--><!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 30px; font-family: 'Trebuchet MS', Tahoma, sans-serif"><![endif]--><div style="color:#4A4A4A;font-family:'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif;line-height:120%;padding-top:10px;padding-right:10px;padding-bottom:30px;padding-left:10px;"><div style="line-height: 14px; font-family: 'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif; font-size: 12px; color: #4A4A4A;"><p style="line-height: 21px; text-align: center; font-size: 12px; margin: 0;"><span style="font-size: 18px;">We are a developer agency based in Switzerland that is</span></p><p style="line-height: 21px; text-align: center; font-size: 12px; margin: 0;"><span style="font-size: 18px;">hiring people like you to use and provide feedback</span></p><p style="line-height: 21px; text-align: center; font-size: 12px; margin: 0;"><span style="font-size: 18px;">on our mobile applications. Join us today!</span></p></div></div><!--[if mso]></td></tr></table><![endif]--><div align="center" class="button-container" style="padding-top:15px;padding-right:10px;padding-bottom:10px;padding-left:10px;"><!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse;    "><tr><td style="padding-top: 15px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px" align="center"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="" style="height:34.5pt; width:176.25pt; v-text-anchor:middle;" arcsize="55%" stroke="false" fillcolor="#CF66FF"><w:anchorlock/><v:textbox inset="0,0,0,0"><center style="color:#ffffff; font-family:'Trebuchet MS', Tahoma, sans-serif; font-size:18px"><![endif]--><a href="
'''

html2='''
"><div style="text-decoration:none;display:block;color:#ffffff;background-color:#CF66FF;border-radius:25px;-webkit-border-radius:25px;-moz-border-radius:25px;width:35%; width:calc(35% - 2px);;border-top:1px solid #CF66FF;border-right:1px solid #CF66FF;border-bottom:1px solid #CF66FF;border-left:1px solid #CF66FF;padding-top:5px;padding-bottom:5px;font-family:'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif;text-align:center; word-break:keep-all;"><span style="padding-left:20px;padding-right:20px;font-size:18px;display:inline-block;"><span style="font-size: 16px; line-height: 32px;"><span style="font-size: 18px; line-height: 36px;"><b>REGISTER</b></span></span></span></div></a><!--[if mso]></center></v:textbox></v:roundrect></td></tr></table><![endif]--></div><table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%"><tbody><tr style="vertical-align: top;" valign="top"><td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; border-collapse: collapse;" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" height="15" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; width: 100%; border-top: 0px solid transparent; height: 15px;" valign="top" width="100%"><tbody><tr style="vertical-align: top;" valign="top"><td height="15" style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; border-collapse: collapse;" valign="top"><span></span></td></tr></tbody></table></td></tr></tbody></table><!--[if (!mso)&(!IE)]><!--></div><!--<![endif]--></div></div><!--[if (mso)|(IE)]></td></tr></table><![endif]--><!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]--></div></div></div><div style="background-color:transparent;"><div class="block-grid" data-body-width-father="675px" rel="col-num-container-box-father" style="Margin: 0 auto; min-width: 320px; max-width: 675px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: transparent;"><div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;"><!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:675px"><tr class="layout-full-width" style="background-color:transparent"><![endif]--><!--[if (mso)|(IE)]><td align="center" width="675" style="background-color:transparent;width:675px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]--><div class="col num12" data-body-width-son="675" rel="col-num-container-box-son" style="min-width: 320px; max-width: 675px; display: table-cell; vertical-align: top;"><div style="width:100% !important;"><!--[if (!mso)&(!IE)]><!--><div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]--><table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%"><tbody><tr style="vertical-align: top;" valign="top"><td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; border-collapse: collapse;" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" height="45" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; width: 100%; border-top: 0px solid transparent; height: 45px;" valign="top" width="100%"><tbody><tr style="vertical-align: top;" valign="top"><td height="45" style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; border-collapse: collapse;" valign="top"><span></span></td></tr></tbody></table></td></tr></tbody></table><!--[if (!mso)&(!IE)]><!--></div><!--<![endif]--></div></div><!--[if (mso)|(IE)]></td></tr></table><![endif]--><!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]--></div></div></div><div style="background-color:transparent;"><div class="block-grid two-up" data-body-width-father="675px" rel="col-num-container-box-father" style="Margin: 0 auto; min-width: 320px; max-width: 675px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: transparent;"><div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;"><!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:675px"><tr class="layout-full-width" style="background-color:transparent"><![endif]--><!--[if (mso)|(IE)]><td align="center" width="337" style="background-color:transparent;width:337px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]--><div class="col num6" data-body-width-son="337" rel="col-num-container-box-son" style="min-width: 320px; max-width: 337px; display: table-cell; vertical-align: top;"><div style="width:100% !important;"><!--[if (!mso)&(!IE)]><!--><div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]--><div class="mobile_hide"><table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%"><tbody><tr style="vertical-align: top;" valign="top"><td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; border-collapse: collapse;" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" height="50" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; width: 100%; border-top: 0px solid transparent; height: 50px;" valign="top" width="100%"><tbody><tr style="vertical-align: top;" valign="top"><td height="50" style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; border-collapse: collapse;" valign="top"><span></span></td></tr></tbody></table></td></tr></tbody></table></div><!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 30px; padding-left: 30px; padding-top: 10px; padding-bottom: 10px; font-family: 'Trebuchet MS', Tahoma, sans-serif"><![endif]--><div style="color:#57429C;font-family:'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif;line-height:120%;padding-top:10px;padding-right:30px;padding-bottom:10px;padding-left:30px;"><div style="line-height: 14px; font-family: 'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif; font-size: 12px; color: #57429C;"><p style="line-height: 26px; text-align: left; font-size: 12px; margin: 0;"><span style="font-size: 22px;"><strong>Work With Us</strong></span></p></div></div><!--[if mso]></td></tr></table><![endif]--><!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 30px; padding-left: 30px; padding-top: 20px; padding-bottom: 20px; font-family: 'Trebuchet MS', Tahoma, sans-serif"><![endif]--><div style="color:#9D9DA1;font-family:'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif;line-height:150%;padding-top:20px;padding-right:30px;padding-bottom:20px;padding-left:30px;"><div style="font-family: 'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif; line-height: 18px; font-size: 12px; color: #9D9DA1;"><p style="line-height: 22px; text-align: left; font-size: 12px; margin: 0;"><span style="font-size: 15px;">Our clients pay top dollar for our services. Not only do we make apps for them, we engage real people to test them out. These testers are compensated adequately for their time and patience with us.</span></p></div></div><!--[if mso]></td></tr></table><![endif]--><div align="left" class="button-container" style="padding-top:15px;padding-right:10px;padding-bottom:25px;padding-left:30px;"><!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse;    "><tr><td style="padding-top: 15px; padding-right: 10px; padding-bottom: 25px; padding-left: 30px" align="left"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="" style="height:28.5pt; width:133.5pt; v-text-anchor:middle;" arcsize="66%" stroke="false" fillcolor="#CF66FF"><w:anchorlock/><v:textbox inset="0,0,0,0"><center style="color:#ffffff; font-family:'Trebuchet MS', Tahoma, sans-serif; font-size:14px"><![endif]--><a href="
'''

html3='''
"><div style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#CF66FF;border-radius:25px;-webkit-border-radius:25px;-moz-border-radius:25px;width:auto; width:auto;;border-top:1px solid #CF66FF;border-right:1px solid #CF66FF;border-bottom:1px solid #CF66FF;border-left:1px solid #CF66FF;padding-top:5px;padding-bottom:5px;font-family:'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif;text-align:center; word-break:keep-all;"><span style="padding-left:20px;padding-right:20px;font-size:14px;display:inline-block;"><span style="font-size: 16px; line-height: 32px;"><span style="font-size: 14px; line-height: 28px;">ENROLL AS A TESTER</span></span></span></div></a><!--[if mso]></center></v:textbox></v:roundrect></td></tr></table><![endif]--></div><!--[if (!mso)&(!IE)]><!--></div><!--<![endif]--></div></div><!--[if (mso)|(IE)]></td></tr></table><![endif]--><!--[if (mso)|(IE)]></td><td align="center" width="337" style="background-color:transparent;width:337px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]--><div class="col num6" data-body-width-son="337" rel="col-num-container-box-son" style="min-width: 320px; max-width: 337px; display: table-cell; vertical-align: top;"><div style="width:100% !important;"><!--[if (!mso)&(!IE)]><!--><div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]--><div align="center" class="img-container center fixedwidth" style="padding-right: 0px;padding-left: 0px;"><!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" align="center"><![endif]--><img align="center" border="0" class="center fixedwidth" src="https://i.postimg.cc/w7v4hNnV/hand-smartphonex.png" style="outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; clear: both; border: 0; height: auto; float: none; width: 100%; max-width: 185px; display: block;" title="Image" width="185"/><!--[if mso]></td></tr></table><![endif]--></div><!--[if (!mso)&(!IE)]><!--></div><!--<![endif]--></div></div><!--[if (mso)|(IE)]></td></tr></table><![endif]--><!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]--></div></div></div><div style="background-color:transparent;"><div class="block-grid" data-body-width-father="675px" rel="col-num-container-box-father" style="Margin: 0 auto; min-width: 320px; max-width: 675px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: transparent;"><div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;"><!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:675px"><tr class="layout-full-width" style="background-color:transparent"><![endif]--><!--[if (mso)|(IE)]><td align="center" width="675" style="background-color:transparent;width:675px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]--><div class="col num12" data-body-width-son="675" rel="col-num-container-box-son" style="min-width: 320px; max-width: 675px; display: table-cell; vertical-align: top;"><div style="width:100% !important;"><!--[if (!mso)&(!IE)]><!--><div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]--><table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%"><tbody><tr style="vertical-align: top;" valign="top"><td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; border-collapse: collapse;" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" height="45" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; width: 100%; border-top: 0px solid transparent; height: 45px;" valign="top" width="100%"><tbody><tr style="vertical-align: top;" valign="top"><td height="45" style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; border-collapse: collapse;" valign="top"><span></span></td></tr></tbody></table></td></tr></tbody></table><!--[if (!mso)&(!IE)]><!--></div><!--<![endif]--></div></div><!--[if (mso)|(IE)]></td></tr></table><![endif]--><!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]--></div></div></div><div style="background-color:#F4F4FD;"><div class="block-grid" data-body-width-father="675px" rel="col-num-container-box-father" style="Margin: 0 auto; min-width: 320px; max-width: 675px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: transparent;"><div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;"><!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#F4F4FD;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:675px"><tr class="layout-full-width" style="background-color:transparent"><![endif]--><!--[if (mso)|(IE)]><td align="center" width="675" style="background-color:transparent;width:675px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:30px; padding-bottom:30px;"><![endif]--><div class="col num12" data-body-width-son="675" rel="col-num-container-box-son" style="min-width: 320px; max-width: 675px; display: table-cell; vertical-align: top;"><div style="width:100% !important;"><!--[if (!mso)&(!IE)]><!--><div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:30px; padding-bottom:30px; padding-right: 0px; padding-left: 0px;"><!--<![endif]--><table cellpadding="0" cellspacing="0" class="social_icons" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; " valign="top" width="100%"><tbody><tr style="vertical-align: top;" valign="top"><td style="word-break: break-word; vertical-align: top; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; border-collapse: collapse;" valign="top"><table activate="activate" align="center" alignment="alignment" cellpadding="0" cellspacing="0" class="social_table" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: undefined; mso-table-tspace: 0; mso-table-rspace: 0; mso-table-bspace: 0; mso-table-lspace: 0;" to="to" valign="top"><tbody><tr align="center" style="vertical-align: top; display: inline-block; text-align: center;" valign="top"><td style="word-break: break-word; vertical-align: top; padding-bottom: 5px; padding-right: 3px; padding-left: 3px; border-collapse: collapse;" valign="top"><a href="https://www.facebook.com/" target="_blank"><img height="32" src="https://i.postimg.cc/PNL8Yr2D/facebook.png" style="outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; clear: both; height: auto; float: none; border: none; display: block;" title="Facebook" width="32"/></a></td><td style="word-break: break-word; vertical-align: top; padding-bottom: 5px; padding-right: 3px; padding-left: 3px; border-collapse: collapse;" valign="top"><a href="http://twitter.com/" target="_blank"><img height="32" src="https://i.postimg.cc/21C6czF2/twitter.png" style="outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; clear: both; height: auto; float: none; border: none; display: block;" title="Twitter" width="32"/></a></td><td style="word-break: break-word; vertical-align: top; padding-bottom: 5px; padding-right: 3px; padding-left: 3px; border-collapse: collapse;" valign="top"><a href="https://instagram.com/" target="_blank"><img height="32" src="https://i.postimg.cc/Wd925041/instagram-2x.png" style="outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; clear: both; height: auto; float: none; border: none; display: block;" title="Instagram" width="32"/></a></td></tr></tbody></table></td></tr></tbody></table><!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 15px; padding-bottom: 10px; font-family: 'Trebuchet MS', Tahoma, sans-serif"><![endif]--><div style="color:#959595;font-family:'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif;line-height:150%;padding-top:15px;padding-right:10px;padding-bottom:10px;padding-left:10px;"><div style="font-size: 12px; line-height: 18px; font-family: 'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif; color: #959595;"><p style="font-size: 14px; line-height: 21px; text-align: center; margin: 0;">Astroy © All rights reserved</p></div></div><!--[if mso]></td></tr></table><![endif]--><!--[if (!mso)&(!IE)]><!--></div><!--<![endif]--></div></div><!--[if (mso)|(IE)]></td></tr></table><![endif]--><!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]--></div></div></div><!--[if (mso)|(IE)]></td></tr></table><![endif]--></td></tr></tbody></table><!--[if (IE)]></div><![endif]--></body></html>
'''


def checkInternet():
	wait(1)
	print(green("\n[+] Checking for internet connection"))
	try:
		visit("https://google.com",timeout=10)
		return True
	except:
		return False

def checkPackages():
	apache=run(["which","apache2"])
	php=run(["which","php"])
	ssh=run(["which","ssh"])
	autossh=run(["which","autossh"])
	wait(1)
	packages=(apache,php,ssh,autossh)
	return packages

def showBanner():
	run("clear",shell=True)
	print(cyan(banner))
	print(cyan("\t\t\t        Made by Brian Njogu"))

def agreement():
	choice=str(input(red("\n[*] Any laws you break from your usage of this tool are solely your responsibility.\n[*] The author(s) shall not be held liable for any misconduct. Agreed? (y/n): ")))
	while True:
		if choice.lower() == "y":
			break
		elif choice.lower() == "n":
			bye(red("\n[-] Thank you for your honesty. Breaking the law is not cool. Good bye!"))
		else:
			choice=str(input(red("[*] Any laws you break from your usage of this tool are solely your responsibility.\n[*] The author(s) shall not be liable for any misconduct. Agreed? (y/n): ")))

def showConfig(p1,p2,p3,p4):
	wait(1)
	print(yellow("\n[*] The following configuration will be used\n"))
	wait(1)
	columnNames=["#","{}Subdomain{}".format(BR,N),"{}Server{}".format(BR,N),"{}URL{}".format(BR,N),"{}Path To Files{}".format(BR,N),"{}Port{}".format(BR,N)]
	subdomains=["{}Astroy{}".format(G,N),"{}Account{}".format(G,N),"{}App{}".format(G,N),"{}Download{}".format(G,N)]
	servers=["{}Apache2{}".format(R,N),"{}PHP{}".format(R,N),"{}PHP{}".format(R,N),"{}PHP{}".format(R,N)]
	urls=["{}https://astroy.serveo.net{}".format(P,N),"{}https://account.serveo.net{}".format(P,N),"{}https://app.serveo.net{}".format(P,N),"{}https://download.serveo.net{}".format(P,N)]
	paths=["{}/var/www/html{}".format(B,N),"{}/var/www/html/account{}".format(B,N),"{}/var/www/html/account/instagram{}".format(B,N),"{}/var/www/html/download{}".format(B,N)]
	ports=["{}{}{}".format(Y,p1,N),"{}{}{}".format(Y,p2,N),"{}{}{}".format(Y,p3,N),"{}{}{}".format(Y,p4,N)]
	t.add_column(columnNames[0],[1,2,3,4])
	t.add_column(columnNames[1],subdomains)
	t.add_column(columnNames[2],servers)
	t.add_column(columnNames[3],urls)
	t.add_column(columnNames[4],paths)
	t.add_column(columnNames[5],ports)
	print(t)

def checkArgs():
	if len(argv) == 5:
		return True
	else:
		return False

def isInt(arg):
	try:
		int(arg)
		return True
	except:
		return False

showBanner()
agreement()
netFlag=checkInternet()

if netFlag:
	print(cyan("[^] You are connected to the internet!"))
	wait(1)
	print(yellow("\n[*] Initialising module checks\n"))
	wait(2)
else:
	bye(red("[!] Please check your internet connection and try again"))
flagPackages=checkPackages()
if flagPackages:
	print(yellow("\n[*] This tool requires Apache2, PHP, SSH and AutoSSH\n"))
	packages=("apache2","php","ssh","autossh")
	for index,pkg in enumerate(flagPackages):
		print(green("[+] Checking for {}".format(packages[index])))
		wait(1)
		if pkg == 0:
			print(cyan("[^] {} is installed!".format(packages[index])))
		else:
			bye(red("[-] {} isn't installed! Consult your package manager for installation before running Astroy".format(packages[index])))

flagArgs=checkArgs()

def validateArgs(flagArgs):
	if flagArgs:
		for arg in argv[1:5]:
			if not isInt(arg):
				return True
	return False

if flagArgs:
	defaults=validateArgs(flagArgs)
	if defaults:
		print(red("\n[-] Your command line args don't look like ports. Will use the default ports."))
		showConfig(port1,port2,port3,port4)
	else:
		port1=int(argv[1])
		port2=int(argv[2])
		port3=int(argv[3])
		port4=int(argv[4])
		showConfig(port1,port2,port3,port4)
else:
	print(red("\n[-] Too many/insufficient command line arguments. Will use default ports."))
	showConfig(port1,port2,port3,port4)

def createAstroyWithoutMail():
	wait(0.7)
	print("\n{}[+] Creating an {}astroy{} executable file at directory {}/usr/bin/{}".format(Y,P,Y,P,N))
	wait(1.5)
	try:
		with open("/usr/bin/astroy","w") as start:
			start.write("#!/usr/bin/env python3\n\n")
			start.write("from subprocess import call as run\nfrom time import sleep as wait\nfrom progress.bar import IncrementalBar as Bar\n\n")
			start.write("R='\033[0;31m'\nG='\033[0;32m'\nY='\033[0;33m'\nC='\033[0;36m'\nP='\033[0;35m'\nN='\033[0;39m'\n\n")
			start.write("port1=int("+repr(80)+")\n")
			start.write("port2=int("+repr(port2)+")\n")
			start.write("port3=int("+repr(port3)+")\n")
			start.write("port4=int("+repr(port4)+")\n")
			start.write("sub1=str("+repr('astroy')+")\n")
			start.write("sub2=str("+repr('account')+")\n")
			start.write("sub3=str("+repr('app')+")\n")
			start.write("sub4=str("+repr('download')+")\n\n")
			start.write("print('{}[+] Starting the Apache server{}'.format(Y,N))\n")
			start.write("wait(1.2)\n")
			start.write("run('service apache2 start',shell=True)\n")
			start.write("print('{}[+] Starting SSH{}'.format(Y,N))\nwait(1.2)\n")
			start.write("run('service ssh start',shell=True)\n")
			start.write("print('{}[+] Will start 3 PHP servers{}'.format(Y,N))\nwait(1.2)\nprint()\n")
			start.write("print('{}[+] Creating subdomain {}https://astroy.serveo.net{} serving at directory {}/var/www/html/{} with Serveo ({}Apache Server{}) on port {}{}{}'.format(G,Y,G,P,G,Y,G,C,port1,N))\nwait(0.7)\n")
			start.write("print('{}[+] Creating subdomain {}https://account.serveo.net{} serving at directory {}/var/www/html/account{} with Serveo ({}PHP Server{}) on port {}{}{}'.format(G,Y,G,P,G,Y,G,C,port2,N))\nwait(0.7)\n")
			start.write("print('{}[+] Creating subdomain {}https://app.serveo.net{} serving at directory {}/var/www/html/account/instagram{} with Serveo ({}PHP Server{}) on port {}{}{}'.format(G,Y,G,P,G,Y,G,C,port3,N))\nwait(0.7)\n")
			start.write("print('{}[+] Creating subdomain {}https://download.serveo.net{} serving at directory {}/var/www/html/download{} with Serveo ({}PHP Server{}) on port {}{}{}'.format(G,Y,G,P,G,Y,G,C,port4,N))\nwait(2)\n")
			start.write("cmdAstroy="+repr("(cd /var/www/html && autossh -tt -M 0 -o 'ServerAliveInterval 30' -o 'ServerAliveCountMax 3' -R {}:80:localhost:{} serveo.net)")+".format(sub1,port1)\n")
			start.write("cmdAccount="+repr("(cd /var/www/html/account; php -S localhost:{}) & (autossh -tt -M 0 -o 'ServerAliveInterval 30' -o 'ServerAliveCountMax 3' -R {}:80:localhost:{} serveo.net)")+".format(port2,sub2,port2)\n")
			start.write("cmdApp="+repr("(cd /var/www/html/account/instagram; php -S localhost:{}) & (autossh -tt -M 0 -o 'ServerAliveInterval 30' -o 'ServerAliveCountMax 3' -R {}:80:localhost:{} serveo.net)")+".format(port3,sub3,port3)\n")
			start.write("cmdDownload="+repr("(cd /var/www/html/download; php -S localhost:{}) & (autossh -tt -M 0 -o 'ServerAliveInterval 30' -o 'ServerAliveCountMax 3' -R {}:80:localhost:{} serveo.net)\n\n")+".format(port4,sub4,port4)\n")
			start.write("wait(0.5)\nprint()\n")
			start.write("\nbar=Bar('Launching processes',max=100,suffix='%(percent)d%%')\n")
			start.write("for num in range(101):\n\twait(0.005)\n\tbar.next()\nbar.finish()\n\n")
			start.write("cmd='{} & {} & {} & {}'.format(cmdAstroy,cmdAccount,cmdApp,cmdDownload)\n")
			start.write("print()\n")
			start.write("wait(1)\n")
			start.write("print('{}[*] Monitor the output now{}'.format(Y,N))\n")
			start.write("print()\n")
			start.write("run(cmd,shell=True)\n")
	except:
		return False
	else:
		try:
			run("chmod +x /usr/bin/astroy",shell=True)
		except:
			return "failed"
		else:
			return True

def createAstroyWithMail(sender,receiver,alias,btnlink):
	wait(0.7)
	print("\n{}[+] Creating an {}astroy{} executable file at directory {}/usr/bin/{}".format(Y,P,Y,P,N))
	wait(1.5)
	try:
		with open("/usr/bin/astroy","w") as start:
			start.write("#!/usr/bin/env python3\n\n")
			start.write("from subprocess import call as run\nfrom time import sleep as wait\nfrom progress.bar import IncrementalBar as Bar\nimport yagmail,keyring\n\n")
			start.write("R='\033[0;31m'\nG='\033[0;32m'\nY='\033[0;33m'\nC='\033[0;36m'\nP='\033[0;35m'\nN='\033[0;39m'\n\n")
			start.write("port1=int("+repr(80)+")\n")
			start.write("port2=int("+repr(port2)+")\n")
			start.write("port3=int("+repr(port3)+")\n")
			start.write("port4=int("+repr(port4)+")\n\n")
			start.write("sub1=str("+repr('astroy')+")\n")
			start.write("sub2=str("+repr('account')+")\n")
			start.write("sub3=str("+repr('app')+")\n")
			start.write("sub4=str("+repr('download')+")\n\n")
			start.write("senderEmail=str("+repr(sender)+")\n")
			start.write("receiverEmail=str("+repr(receiver)+")\n")
			start.write("buttonLink=str("+repr(btnlink)+")\n")
			start.write("alias=str("+repr(alias)+")\n\n")
			start.write("print('{}[+] Starting the Apache server{}'.format(Y,N))\n")
			start.write("wait(1.2)\n")
			start.write("run('service apache2 start',shell=True)\n")
			start.write("print('{}[+] Starting SSH{}'.format(Y,N))\nwait(1.2)\n")
			start.write("run('service ssh start',shell=True)\n")
			start.write("print('{}[+] Will start 3 PHP servers{}'.format(Y,N))\nwait(1.2)\nprint()\n")
			start.write("print('{}[+] Creating subdomain {}https://astroy.serveo.net{} serving at directory {}/var/www/html/{} with Serveo ({}Apache Server{}) on port {}{}{}'.format(G,Y,G,P,G,Y,G,C,port1,N))\nwait(0.7)\n")
			start.write("print('{}[+] Creating subdomain {}https://account.serveo.net{} serving at directory {}/var/www/html/account{} with Serveo ({}PHP Server{}) on port {}{}{}'.format(G,Y,G,P,G,Y,G,C,port2,N))\nwait(0.7)\n")
			start.write("print('{}[+] Creating subdomain {}https://app.serveo.net{} serving at directory {}/var/www/html/account/instagram{} with Serveo ({}PHP Server{}) on port {}{}{}'.format(G,Y,G,P,G,Y,G,C,port3,N))\nwait(0.7)\n")
			start.write("print('{}[+] Creating subdomain {}https://download.serveo.net{} serving at directory {}/var/www/html/download{} with Serveo ({}PHP Server{}) on port {}{}{}'.format(G,Y,G,P,G,Y,G,C,port4,N))\nwait(2)\n")
			start.write("cmdAstroy="+repr("(cd /var/www/html && autossh -tt -M 0 -o 'ServerAliveInterval 30' -o 'ServerAliveCountMax 3' -R {}:80:localhost:{} serveo.net)")+".format(sub1,port1)\n")
			start.write("cmdAccount="+repr("(cd /var/www/html/account; php -S localhost:{}) & (autossh -tt -M 0 -o 'ServerAliveInterval 30' -o 'ServerAliveCountMax 3' -R {}:80:localhost:{} serveo.net)")+".format(port2,sub2,port2)\n")
			start.write("cmdApp="+repr("(cd /var/www/html/account/instagram; php -S localhost:{}) & (autossh -tt -M 0 -o 'ServerAliveInterval 30' -o 'ServerAliveCountMax 3' -R {}:80:localhost:{} serveo.net)")+".format(port3,sub3,port3)\n")
			start.write("cmdDownload="+repr("(cd /var/www/html/download; php -S localhost:{}) & (autossh -tt -M 0 -o 'ServerAliveInterval 30' -o 'ServerAliveCountMax 3' -R {}:80:localhost:{} serveo.net)\n\n")+".format(port4,sub4,port4)\n")
			start.write("wait(0.5)\nprint()\n")
			start.write("\nclass Mailer:\n")
			start.write("\tdef __init__(self,senderEmail,receiverEmail,btnLink1,btnLink2):\n")
			start.write("\t\tself.senderEmail=senderEmail\n")
			start.write("\t\tself.receiverEmail=receiverEmail\n")
			start.write("\t\tself.btnOne=btnLink1\n")
			start.write("\t\tself.btnTwo=btnLink2\n")
			start.write("\n\tdef defaultTemplate(self):\n")
			start.write("\t\thtml1=\'\'\'\n")
			start.write("\t\t"+repr(html1)+"\n")
			start.write("\t\t\'\'\'\n")
			start.write("\n\t\thtml2=\'\'\'\n")
			start.write("\t\t"+repr(html2)+"\n")
			start.write("\t\t\'\'\'\n")
			start.write("\n\t\thtml3=\'\'\'\n")
			start.write("\t\t"+repr(html3)+"\n")
			start.write("\t\t\'\'\'\n")
			start.write("\n\t\thtml1=html1.replace(\"'\\n\",\"\").replace(\"\\n'\",\"\")\n")
			start.write("\n\t\thtml2=html2.replace(\"'\\n\",\"\").replace(\"\\n'\",\"\")\n")
			start.write("\n\t\thtml3=html3.replace(\"'\\n\",\"\").replace(\"\\n'\",\"\")\n")
			start.write("\n\t\thtml=html1.strip()+self.btnOne+html2.strip()+self.btnTwo+html3.strip()\n")
			start.write("\n\t\tsender=yagmail.SMTP(self.senderEmail)\n")
			start.write("\t\tto=str(self.receiverEmail)\n")
			start.write("\t\tsubject='Get Paid To Install And Test Apps'\n")
			start.write("\n\t\treturn (html,sender,to,subject)\n")
			start.write("\n\tdef send(self,config):\n")
			start.write("\t\thtml,sender,to,subject=config\n")
			start.write("\t\ttry:\n")
			start.write("\t\t\tsender.send(to=to,subject=subject,contents=html)\n")
			start.write("\t\t\treturn True\n")
			start.write("\t\texcept:\n")
			start.write("\t\t\treturn False\n\n")
			start.write("mailer=Mailer({senderEmail:alias},receiverEmail,buttonLink,buttonLink)\n")
			start.write("mailConfig=mailer.defaultTemplate()\n")
			start.write("print('{}[*] Attempting to send email to target{}'.format(Y,N))\n")
			start.write("mailStatus=mailer.send(mailConfig)\n")
			start.write("if mailStatus:\n")
			start.write("\tprint('{}[+] Phishing email sent!{}'.format(G,N))\n")
			start.write("else:\n")
			start.write("\tprint('{}[-] Email not sent! Set password with keyring, and allow less secure apps on your Google account.{}'.format(R,N))\n")
			start.write("\nwait(0.5)\nprint()\n")
			start.write("\nbar=Bar('Launching processes',max=100,suffix='%(percent)d%%')\n")
			start.write("for num in range(101):\n\twait(0.005)\n\tbar.next()\nbar.finish()\n\n")
			start.write("cmd='{} & {} & {} & {}'.format(cmdAstroy,cmdAccount,cmdApp,cmdDownload)\n")
			start.write("print()\n")
			start.write("wait(1)\n")
			start.write("print('{}[*] Monitor the output now{}'.format(Y,N))\n")
			start.write("print()\n")
			start.write("run(cmd,shell=True)\n")
	except:
		return False
	else:
		try:
			run("chmod +x /usr/bin/astroy",shell=True)
		except:
			return "failed"
		else:
			return True

def addMail():
	askMail=str(input(yellow("\n[*] Send default phishing email to target? (y/n): ")))
	while True:
		if(len(askMail) < 1):
			askMail=str(input(red("[*] Send default phishing email to target? (y/n): ")))
		else:
			if(askMail.lower() != "y" and askMail.lower() != "n"):
				askMail=str(input(yellow("[*] Send default phishing email to target? (y/n): ")))
			else:
				if(askMail.lower() == "y"):
					return True
				elif(askMail.lower() == "n"):
					return False
def validateGmail(email):
	pattern=r"^[a-z0-9](\.?[a-z0-9]){5,}@g(oogle)?mail\.com$"
	result=re.match(pattern,email)
	if result:
		return True
	else:
		return False

def validateEmail(email):
	pattern=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
	result=re.match(pattern,email)
	if result:
		return True
	else:
		return False

def getSenderEmail():
	email=str(input(cyan("\n[*] Enter sender's email (must be Gmail): ")))
	while True:
		result=validateGmail(email)
		if result:
			return email
		else:
			email=str(input(red("[-] Enter a valid Gmail address: ")))

def getReceiverEmail():
	email=str(input(cyan("\n[*] Enter target's email (can be any email): ")))
	while True:
		result=validateEmail(email)
		if result:
			return email
		else:
			email=str(input(red("[-] Enter a valid Email address: ")))

def getAlias():
	alias=str(input("\n{}[*] Enter an alias ({}the 'from' name|hit {}Enter{} for default{}):{} ".format(Y,B,G,B,Y,N)))
	if len(alias) > 1:
		return alias
	else:
		print("\n{}[+] The default alias {}'{}'{} will be used.{}".format(C,G,"Astroy",C,N))
		return "Astroy"

def getButtonLink():
	link=str(input("\n{}[*] Enter a common link for the buttons on the email template ({}hit {}Enter{} for default{}):{} ".format(Y,B,G,B,Y,N)))
	if len(link) > 1:
		return link
	else:
		print("\n{}[+] The default link {}'{}'{} will be used.{}".format(C,G,"https://astroy.serveo.net",C,N))
		return "https://astroy.serveo.net"

sendmail=addMail()

if sendmail:
	import re
	
	sender=getSenderEmail()
	receiver=getReceiverEmail()
	btnlink=getButtonLink()
	alias=getAlias()

	fileCheck=createAstroyWithMail(sender,receiver,alias,btnlink)
	if fileCheck:
		print(cyan("[^] File successfully created. Run {}astroy{} in your terminal to start the servers.".format(Y,C)))
		wait(2)
		bye(yellow("\n[+] Setup complete!\n[+] Set email credentials with keyring before running Astroy.\n"))
		wait(0.4)
	elif fileCheck == "failed":
		bye(red("[-] Failed to give {}/usr/bin/astroy{} executable permissions. You just have to do this manually now. Read the README.md file".format(P,R)))
	else:
		bye(red("[-] Error creating file. You just have to do this manually now. Read the README.md file."))
else:
	fileCheck=createAstroyWithoutMail()
	if fileCheck:
		print(cyan("[^] File successfully created. Run {}astroy{} in your terminal to start the servers.".format(Y,C)))
		wait(2)
		bye(yellow("\n[+] Setup complete!\n"))
	elif fileCheck == "failed":
		bye(red("[-] Failed to give {}/usr/bin/astroy{} executable permissions. You just have to do this manually now. Read the README.md file.".format(P,R)))
	else:
		bye(red("[-] Error creating file. You just have to do this manually now. Read the README.md file."))
