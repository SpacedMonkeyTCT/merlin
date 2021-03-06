{% from 'macros.tpl' import planetscanslink, galaxyscanslink with context %}
<table cellpadding="3" cellspacing="1" class="black">
    <tr class="datahigh"><th colspan="6">{{ title }}</th></tr>
    <tr class="header">
        <th>Coords</th>
        <th>Tick</th>
        <th>Type</th>
        <th>Link</th>
        <th>Scanned by</th>
    </tr>
    {% for scan in scans %}
    {% with planet = scan.planet %}
    <tr class="{{ loop.cycle('odd', 'even') }}">
        <td class="center"><a {{galaxyscanslink(planet.galaxy)}}>{{ planet.x }}:{{ planet.y }}</a> <a {{planetscanslink(planet)}}>{{ planet.z }}</a></td>
        <td class="center">{{ scan.tick }}</td>
        <td class="center">{{ scan.scantype }}</td>
        <td class="center"><a href="{% url "scan_id", scan.tick, scan.pa_id %}"
                onclick="return linkshift(event, '{{ scan.link|url }}');">{{ scan.pa_id }}</a></td>
        <td class="center">{{ scan.scanner.name }}</td>
    </tr>
    {% endwith %}
    {% endfor %}
</table>
