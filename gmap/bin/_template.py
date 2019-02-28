document = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
	<name>GPS track</name>
    <description>{desc}</description>
	<LookAt>
		<gx:TimeSpan>
			<begin>2015-01-20T13:26:30Z</begin>
			<end>2015-01-20T14:04:00Z</end>
		</gx:TimeSpan>
		<longitude>121.625405</longitude>
		<latitude>25.059674</latitude>
		<altitude>0</altitude>
		<heading>0</heading>
		<tilt>0</tilt>
		<range>2418.240532</range>
	</LookAt>
	<Style id="multiTrack_h">
		<IconStyle>
			<scale>1.2</scale>
			<Icon>
				<href>http://earth.google.com/images/kml-icons/track-directional/track-0.png</href>
			</Icon>
		</IconStyle>
		<LineStyle>
			<color>99ffac59</color>
			<width>8</width>
		</LineStyle>
	</Style>
	<StyleMap id="multiTrack">
		<Pair>
			<key>normal</key>
			<styleUrl>#multiTrack_n</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#multiTrack_h</styleUrl>
		</Pair>
	</StyleMap>
	<Style id="multiTrack_n">
		<IconStyle>
			<Icon>
				<href>http://earth.google.com/images/kml-icons/track-directional/track-0.png</href>
			</Icon>
		</IconStyle>
		<LineStyle>
			<color>99ffac59</color>
			<width>6</width>
		</LineStyle>
	</Style>
	<Folder>
		<name>Tracks</name>
		<Placemark>
			<name>Run at  river side</name>
            <description>{desc}</description>
			<styleUrl>#multiTrack</styleUrl>
			<gx:balloonVisibility>1</gx:balloonVisibility>
			<gx:Track>
                {times}
				{coords}
			</gx:Track>
		</Placemark>
	</Folder>
</Document>
</kml>"""

time = "<when>{dtime}</when>\n"
coord = "<gx:coord>{lon} {lat} {alt}</gx:coord>\n"
