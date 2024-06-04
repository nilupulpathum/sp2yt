from setuptools import setup, find_packages

setup(
    name='sp2yt',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'spotipy',
        'yt-dlp',
        'pydub',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'sp2yt = sp2yt.sp2yt:main'
        ]
    },
    include_package_data=True,
    description='A CLI tool to download Spotify playlists as YouTube MP3s',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Nilupul Pathum',
    author_email='n.pathumliyanarachchi@gmail.com',
    url='https://github.com/npathum2004/sp2yt',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
