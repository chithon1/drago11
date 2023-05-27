FROM qithoniq/drago:slim-buster

 #clonning repo 
 RUN git clone https://github.com/qithoniq/drago.git /root/drago
 #working directory 
 WORKDIR /root/drago
 RUN apk add --update --no-cache p7zip
 # Install requirements
 RUN pip3 install --no-cache-dir -r requirements.txt
 ENV PATH="/home/drago/bin:$PATH"
 CMD ["python3","-m","drago"]
