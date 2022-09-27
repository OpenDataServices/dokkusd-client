def get_remote_name_of_url(git_remote_verbose_output, url_wanted):
    for line in git_remote_verbose_output.split("\n"):
        line_bits = [i.strip() for i in line.split() if i.strip()]
        if line_bits and line_bits[1] == url_wanted:
            return line_bits[0]
