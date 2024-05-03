from setuptools import find_packages, setup

package_name = 'desenhador'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='seu-nome',
    maintainer_email='seu-email',
    description='sua-descrição',
    license='CC0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "teste = desenhador.hello:main",
            "teste2 = desenhador.goodbye:teste",
            "desenho = desenhador.desenhotrue:main",
        ],
    },
)