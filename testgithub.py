import requests
import json

##Parameters that you can change
mail_list      = [{"email_id":"roja.p@corefactors.in"}]
subject      = "This is the subject"
html_content = "<html><head><title></title></head><body><p><a href='http://www.corefactors.in'> Link</a></p></body></html>"
##end

message = {
           "html_content":html_content,
           "subject":subject,
           "from_mail":"info@swarnakanchi.com",
           "from_name":"swarnakanchi",
           "reply_to":"info@swarnakanchi.com",
           "to_recipients":mail_list
           }

url     = "http://in/send-email-json-otom/be851b60-583e-42b7-868b-00467469c1da/1008/"
payload = {"mail_datas":
                    {"message": message}
          } 
reqdata = requests.post(url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
print (reqdata.content)
print "completed"
