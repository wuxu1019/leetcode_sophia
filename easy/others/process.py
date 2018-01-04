import subprocess
try:
    subprocess.call([tool_path + '/create_gota.sh',android_target,gotacmd_lversion,gotacmd_kk])
except subprocess.CalledProcessError as e:
    raise Exception('GOTA script failed, {}'.format(e.returncode))
except Exception as e:
raise Exception('Error executing GOTA script, {}'.format(e))
