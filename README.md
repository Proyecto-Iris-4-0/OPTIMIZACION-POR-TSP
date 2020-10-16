# OPTIMIZACION-POR-TSP
En este repositorio se encuentra el código utilizado para realizar TSP's sobre las rutas.
Para poder ejecutarlo es necesario tener instalada la librería de Gurobi para Python. 

Lo que hace es generar una estructura que se pueda exportar fácilmente a un HPC y hacer varias ejecuciones simultáneas utilizando el programa de encolado de procesos SLURM. Se parte de un conjunto de rutas sin optimizar almacenadas en una base de datos MongoDB y se prepara el entorno necesario (datos de entrada y código) para que haya una ejecución por cada ruta.
