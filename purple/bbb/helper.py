from bs4 import BeautifulSoup
import requests
import hashlib



class BigBlueButton:
    def __init__(self):
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
            'Content-Type': 'application/xml;charset=UTF-8'
        }
        self.url = "https://meet.gedik.edu.tr/bigbluebutton/"
        self.secret_key = "F5vlGEMNuuuCRFkVnEx9RCtiHuKRndJtDepadfqRCA"
    
    def meet_control(self):
        result = requests.get(self.url, headers=self.headers).text
        parser = BeautifulSoup(result,"lxml")
        return parser.find("returncode").text

    def join_meet_mod(self,meetingID,password):
        __fullname = "Uzem+Destek"
        __meetingID = meetingID
        __password = password
        __url = self.EncryptBBB("join",f"fullName={__fullname}&meetingID={__meetingID}&password={__password}&redirect=true")
        return __url

    def get_meetings(self):
        data = []
        __url = self.EncryptBBB("getMeetings")
        result = requests.get(__url, headers=self.headers).text
        parser = BeautifulSoup(result, "xml")
        find_meeting = parser.find_all("meeting")

        for meeting in find_meeting:
            mods = []
            users = []
            user_count = 0
            if meeting.find('bbb-context-name') is None:
                continue
            for attendee in meeting.find("attendees"):
                
                user = {
                    'userID': str(attendee.find("userID"))[8:-9],
                    'fullName': str(attendee.find("fullName"))[10:-11],
                    'role' : str(attendee.find("role"))[6:-7],
                }
                if user['userID'] == '':
                    continue
                elif user['role'] == 'MODERATOR':
                    user_count+=1
                    mods.append(user)
                else:
                    user_count+=1
                    users.append(user)

            json_data = {
                'meetingName' : meeting.find("meetingName").text,
                'meetingID' :meeting.find("meetingID").text,
                'internalMeetingID' : meeting.find("internalMeetingID").text,
                'joinMeet': meeting.find("moderatorPW").text,
                'createDate' : meeting.find("createDate").text,
                'recording' : meeting.find("recording").text,
                'bbb-context-name' : meeting.find('bbb-context-name').text,
                'join_url' : self.join_meet_mod(meeting.find("meetingID").text,meeting.find("moderatorPW").text),
                'userCount' : user_count,
                'users': users,
                'mods' : mods
            }
            data.append(json_data)
            return data


    def EncryptBBB(self,api_name, query=False):
        __api_name = api_name.encode("utf-8")
        __secret_key = self.secret_key.encode("utf-8")

        hash = hashlib.sha256()
        hash.update(__api_name)
        
        if  query != False:
            __query = query.encode("utf-8")
            hash.update(__query)
        
        hash.update(__secret_key)

        checksum = hash.hexdigest()
        if  query != False:
            url = f"{self.url}{api_name}?checksum={checksum}&{query}"
        elif query == False:
            url = f"{self.url}{api_name}?checksum={checksum}"

        return url

if __name__ == '__main__':
    app = BigBlueButton()
    