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
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/sp2yt',  # Replace with your GitHub repo
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
