from subprocess import Popen, PIPE
from tools import parser


def get_message(stderr, type):
    """
    used to return exit messages from command execution
    """
    response = []
    for line in stderr.split('\n'):
        ret = parser.parse_line(line)
        if ret and ret['type'] == type:
            if not 'swaps' in ret['content']:
                response.append(ret['content'])
    return response


def execute(cmd):
    """
    execute given cmd. return boolean based on exit status and error string
    """
    p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = p.communicate()
    p_status = p.wait()
    if p_status == 0:
        return True, get_message(stderr, 'success')
    else:
        return False, get_message(stderr, 'error')


def sanitize_passphrase(passphrase):
    """
    Used to avoid errors with passphrase which includes spaces
    """
    return ''.join(['"', passphrase, '"'])


def tdig(tombfile, size):
    """
    Usage: tdig <tombfilename> <size> - dig a tomb of given size
    """

    cmd = ' '.join(['tomb', 'dig', tombfile, '-s', str(size), '--no-color'])
    return execute(cmd)


def tforge(keyfile, passphrase):
    """
    Usage: tforge <keyfile> <passphrase> - forge a key with given passphrase
    """
    cmd = ' '.join(['tomb',
        'forge',
        keyfile,
        '--unsecure-dev-mode',
        '--tomb-pwd',
        sanitize_passphrase(passphrase),
        '--no-color'])
    return execute(cmd)


def tlock(tombfile, keyfile, passphrase):
    cmd = ' '.join(['tomb',
        'lock',
        tombfile,
        '-k',
        keyfile,
        '--unsecure-dev-mode',
        '--tomb-pwd',
        sanitize_passphrase(passphrase),
        '--no-color'])
    return execute(cmd)


def topen(tombfile, keyfile, passphrase, mountpath=False):
    if not mountpath:
        mountpath = ''
    cmd = ' '.join(['tomb',
        'open',
        tombfile,
        '-k',
        keyfile,
        '--unsecure-dev-mode',
        '--tomb-pwd',
        sanitize_passphrase(passphrase),
        '--no-color',
        mountpath])
    return execute(cmd)


def tclose(tombfile):
    cmd = ' '.join(['tomb', 'close', tombfile, '--no-color'])
    return execute(cmd)


def tresize(tombfile, keyfile, passphrase, newsize):
    cmd = ' '.join(['tomb',
        'resize',
        tombfile,
        '-k',
        keyfile,
        '--unsecure-dev-mode',
        '--tomb-pwd',
        sanitize_passphrase(passphrase),
        '-s',
        str(newsize),
        '--no-color'])
    return execute(cmd)


def tbury(keyfile, passphrase, imagefile):
    cmd = ' '.join(['tomb',
        'bury',
        '-k',
        keyfile,
        '--unsecure-dev-mode',
        '--tomb-pwd',
        sanitize_passphrase(passphrase),
        imagefile,
        '--no-color'])
    return execute(cmd)


def texhume(keyfile, passphrase, imagefile):
    cmd = ' '.join(['tomb',
        'exhume',
        '-k',
        keyfile,
        '--unsecure-dev-mode',
        '--tomb-pwd',
        sanitize_passphrase(passphrase),
        imagefile,
        '--no-color'])
    return execute(cmd)


def tpasswd(keyfile, newpassphrase, oldpassphrase):
    cmd = ' '.join(['tomb',
        'passwd',
        '-k',
        keyfile,
        '--unsecure-dev-mode',
        '--tomb-pwd',
        sanitize_passphrase(newpassphrase),
        '--tomb-old-pwd',
        sanitize_passphrase(oldpassphrase),
        '--no-color'])
    return execute(cmd)


def tsetkey(oldkeyfile, tombfile, newkeyfile, newpassphrase, oldpassphrase):
    cmd = ' '.join(['tomb',
        'setkey',
        oldkeyfile,
        '-k',
        newkeyfile,
        '--unsecure-dev-mode',
        '--tomb-pwd',
        sanitize_passphrase(newpassphrase),
        '--tomb-old-pwd',
        sanitize_passphrase(oldpassphrase),
        '--no-color'])
    return execute(cmd)
