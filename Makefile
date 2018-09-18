install:
	poetry install
	poetry run jupyter labextension install \@jupyter-widgets/jupyterlab-manager
	poetry run jupyter labextension install jupyter-leaflet


lab:
	poetry run jupyter lab .
