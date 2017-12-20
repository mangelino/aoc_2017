FROM continuumio/miniconda
RUN conda install jupyter matplotlib -y
RUN pip install prettytable
VOLUME /opt/notebooks
EXPOSE 8888
CMD ["jupyter","notebook","--allow-root","--ip='*'","--notebook-dir=/opt/notebooks"]
