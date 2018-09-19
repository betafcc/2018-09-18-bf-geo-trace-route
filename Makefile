install:
	poetry install
	poetry run jupyter labextension install \@jupyter-widgets/jupyterlab-manager
	poetry run jupyter labextension install jupyter-leaflet
	$(MAKE) geolitedb


lab:
	poetry run jupyter lab .


geolitedb:
	mkdir -p data
	wget "http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz" -P data
	tar -xf data/GeoLite2-City.tar.gz -C data/
	rm data/GeoLite2-City.tar.gz
	mv data/GeoLite2-City_*/GeoLite2-City.mmdb ./data
	rm -rf data/GeoLite2-City_*
