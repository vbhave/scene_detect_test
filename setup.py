from setuptools import setup, find_packages

package_data = {

}

setup(name='scene_detection',
      version='0.1',
      description='Helps in labeling the scene and detecting scene attributes',
      url='https://github.com/UMass-Rescue/scene_detection',
      author='Vivek Bhave, Prasanna Lakkur Subramanyam',
      author_email='vbhave@umass.edu, psubramanyam@umass.edu',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
            'torchvision>=0.5.0',
            'opencv_python>=4.1.2.30',
            'torch>=1.4.0',
            'numpy>=1.18.1',
            'Pillow>=7.1.1'
      ],
      zip_safe=False)