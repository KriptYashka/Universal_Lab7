import re

classic_cmd = {
    r"прив|здравств": user_profile_edit.registration,
    r"ы": help.send_help_text
}