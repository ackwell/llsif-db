# LoveLive: School Idol Festival - Database

A card database for the LoveLive: School Idol Festival mobile game.

**Planned features:**
- [x] Database of cards and relevant data (mostly complete)
- [ ] User accounts with opt-in listing in friend finder
- [ ] 'Collection manager' thingy with best-team-for-song-X whatsit
- [ ] Perhaps a random draw emulator?
- [ ] Event / daily song tracker (per region)
- [ ] Open to suggestions!

**Current Stack:**
- Python 2.7
	- Flask
	- SQLAlchemy
	- WTForms
	- (various bindings between the above)
- MySQL (I use MariaDB 10, though any MySQL distribution should work)
- No client side framework (though I do like the look of angular, if one is needed)

## Setting up

**Required packages:**
- For MySQL-python
	- `libssl-dev`
- For Pillow:
	- `libtiff4-dev`
	- `libjpeg8-dev`
	- `zlib1g-dev`
	- `libfreetype6-dev`
	- `liblcms2-dev`
	- `libwebp-dev`
	- `tcl8.5-dev`
	- `tk8.5-dev`
	- `python-tk`
- For uWSGI (if using to serve)
	- `libpcre3-dev`

Setup / distribution / contributing guides to come.

If you feel you could help out on this project, pull requests are absolutely open - I'll review any requests sent in as soon as I can. Frontend is the area with the least coverage currently, I'm no designer.
