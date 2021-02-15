from pprint import pprint, pformat
import click
import sys
import smartthings


@click.command()
@click.option('--authfile', default='access_token.secret', type=click.Path())
@click.argument('argv', required=False, nargs=-1)
def main(authfile, argv):
    smartclient = smartthings.SmartThingsClient(tokenfile=authfile)
    device_list = smartclient.list_devices()

    for arg in argv:
        matching_devices = []
        try:
            (name, set_state) = arg.split('=', 2)
            set_state = set_state.strip()
        except ValueError:
            # did not supply an '=state' directive
            name = arg
            set_state = None

        for dev in device_list['items']:
            if name.lower() in dev['label'].lower():
                # print(f"Found matching device: '{dev['label']}', ID {dev['deviceId']}")
                matching_devices.append({
                    'name': dev['label'],
                    'id': dev['deviceId']
                })

        if len(matching_devices) == 0:
            print(f"No devices matching '{name}'")
        elif len(matching_devices) == 1:
            device = matching_devices[0]
            # desc = smartclient.describe_device(device['id'])
            status = smartclient.device_status(device['id'])
            # pprint(desc.items())
            # pprint(status.items())
            current_status = status['light']['switch']['value']
            print(f"{device['name']} is {current_status}")
            if set_state is None or len(set_state) == 0:
                pass # do nothing
            elif set_state == current_status:
                print(f" -> It's already {current_status}, leaving it alone")
            else:
                print(f" -> Setting {device['name']} to {set_state}")
                smartclient.switch(device['id'], set_state)
        else:
            print(f"Multiple devices match '{arg}':")
            for device in matching_devices:
                print(f" - {device['name']}")


main()