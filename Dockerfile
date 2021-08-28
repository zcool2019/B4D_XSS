FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt install -y php python3 python3-pip wget firefox
RUN pip3 install selenium
COPY bin/geckodriver /usr/local/bin/geckodriver
COPY httpd.sh /httpd.sh
RUN chmod +x /httpd.sh
COPY www /www
COPY xss_bot.py /xss_bot.py
#ENTRYPOINT ["bash","/httpd.sh","&"]
CMD ["python3","/xss_bot.py"]
