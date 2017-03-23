#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from __future__ import print_function

import argparse
import getpass

import erppeek

from odoo_api import *


def get_arguments():

    global server
    global username
    global password
    global dbname
    global db_server
    global db_user
    global db_password

    parser = argparse.ArgumentParser()
    parser.add_argument('--server', action="store", dest="server")
    parser.add_argument('--user', action="store", dest="username")
    parser.add_argument('--pw', action="store", dest="password")
    parser.add_argument('--db', action="store", dest="dbname")
    parser.add_argument('--dbserver', action="store", dest="db_server")
    parser.add_argument('--dbu', action="store", dest="db_user")
    parser.add_argument('--dbw', action="store", dest="db_password")

    args = parser.parse_args()
    print('%s%s' % ('--> ', args))

    if args.server is not None:
        server = args.server
    elif server == '*':
        server = raw_input('server: ')

    if args.dbname is not None:
        dbname = args.dbname
    elif dbname == '*':
        dbname = raw_input('dbname: ')

    if args.username is not None:
        username = args.username
    elif username == '*':
        username = raw_input('username: ')

    if args.password is not None:
        password = args.password
    elif password == '*':
        password = getpass.getpass('password: ')

    if args.db_server is not None:
        db_server = args.db_server
    elif db_server == '*':
        db_server = getpass.getpass('db_server: ')

    if args.db_user is not None:
        db_user = args.db_user
    elif db_user == '*':
        db_user = getpass.getpass('db_user: ')

    if args.db_password is not None:
        db_password = args.db_password
    elif db_password == '*':
        db_password = getpass.getpass('db_password: ')


def secondsToStr(t):

    return "%d:%02d:%02d.%03d" % reduce(lambda ll, b: divmod(ll[0], b) + ll[1:], [(t * 1000,), 1000, 60, 60])


def buffer():
    pass


if __name__ == '__main__':

    server = 'http://localhost:8069'
    # server = '*'

    username = 'username'
    # username = '*'
    password = 'password'
    # password = '*'

    dbname = 'odoo'
    # dbname = '*'

    db_server = 'localhost'
    # db_server = '*'

    db_user = 'openerp'
    # db_user = '*'

    db_password = 'openerp'
    # db_password = '*'

    print()
    print('--> setup.py...')
    print('--> server:', server)

    get_arguments()

    from time import time
    start = time()

    client = erppeek.Client(server, dbname, username, password)
    conn_string = "dbname='" + dbname + "' user='" + db_user + "' host='" + db_server + \
                  "' password='" + db_password + "'"

    #
    # tk-openerp-vm-fmng
    #

    # # python setup.py --server 'http://tk-openerp-vm-fmng:8069' --user 'cvercelino' --pw '*' --db 'cv_fmng_pro'
    # file_args = []
    # db_path = 'data/fmng.sqlite'
    # table_name = 'clv_mfile'
    # print('-->', client, file_args, db_path, table_name)
    # print('--> Executing fmng_entity_export_sqlite()...')
    # print()
    # fmng_entity_export_sqlite(client, file_args, db_path, table_name)

    #
    # tkl-odoo-vm-fmng
    #

    # # python setup.py --server 'http://tkl-odoo-vm-fmng:8069' --user 'carlos@vercelino.com' --pw '*' --db 'vfmng_pro'
    # global_tag_args = []
    # db_path = 'data/vfmng.sqlite'
    # table_name = 'clv_global_tag'
    # print('-->', client, global_tag_args, db_path, table_name)
    # print('--> Executing clv_tag_export_sqlite()...')
    # print()
    # clv_tag_export_sqlite(client, global_tag_args, db_path, table_name)

    # # python setup.py --server 'http://tkl-odoo-vm-fmng:8069' --user 'carlos@vercelino.com' --pw '*' --db 'vfmng_pro'
    # mfile_category_args = []
    # db_path = 'data/vfmng.sqlite'
    # table_name = 'clv_mfile_category'
    # print('-->', client, mfile_category_args, db_path, table_name)
    # print('--> Executing clv_file_category_export_sqlite()...')
    # print()
    # clv_file_category_export_sqlite(client, mfile_category_args, db_path, table_name)

    # # python setup.py --server 'http://tkl-odoo-vm-fmng:8069' --user 'carlos@vercelino.com' --pw '*' --db 'vfmng_pro'
    # file_args = []
    # db_path = 'data/vfmng.sqlite'
    # table_name = 'clv_mfile'
    # print('-->', client, file_args, db_path, table_name)
    # print('--> Executing clv_file_export_sqlite()...')
    # print()
    # clv_file_export_sqlite(client, file_args, db_path, table_name)

    #
    # localhost
    #

    # # python setup.py --user 'data.admin' --pw '*' --db 'mfmng_dev'
    # file_args = []
    # db_path = 'data/fmng.sqlite'
    # table_name = 'clv_mfile'
    # print('-->', client, file_args, db_path, table_name)
    # print('--> Executing fmng_entity_import_sqlite()...')
    # print()
    # fmng_entity_import_sqlite(client, file_args, db_path, table_name)

    # # python setup.py --user 'data.admin' --pw '*' --db 'mfmng_dev'
    # global_tag_args = []
    # db_path = 'data/vfmng.sqlite'
    # table_name = 'clv_global_tag'
    # print('-->', client, clv_global_tag, db_path, table_name)
    # print('--> Executing clv_global_tag_import_sqlite()...')
    # print()
    # clv_global_tag_import_sqlite(client, clv_global_tag, db_path, table_name)

    # # python setup.py --user 'data.admin' --pw '*' --db 'mfmng_dev'
    # mfile_category_args = []
    # db_path = 'data/vfmng.sqlite'
    # table_name = 'clv_mfile_category'
    # print('-->', client, mfile_category_args, db_path, table_name)
    # print('--> Executing clv_mfile_category_import_sqlite()...')
    # print()
    # clv_mfile_category_import_sqlite(client, mfile_category_args, db_path, table_name)

    # # python setup.py --user 'data.admin' --pw '*' --db 'mfmng_dev'
    # mfile_args = []
    # db_path = 'data/vfmng.sqlite'
    # table_name = 'clv_mfile'
    # category_table_name = 'clv_mfile_category'
    # tag_table_name = 'clv_global_tag'
    # print('-->', client, mfile_args, db_path, table_name, category_table_name, tag_table_name)
    # print('--> Executing clv_mfile_import_sqlite()...')
    # print()
    # clv_mfile_import_sqlite(client, mfile_args, db_path, table_name, category_table_name, tag_table_name)

    # # python setup.py --user 'data.admin' --pw '*' --db 'mfmng_dev'
    # mfile_args = []
    # db_path = 'data/vfmng.sqlite'
    # table_name = 'clv_mfile'
    # print('-->', client, mfile_args, db_path, table_name)
    # print('--> Executing clv_mfile_import_parent_id_sqlite()...')
    # print()
    # clv_mfile_import_parent_id_sqlite(client, mfile_args, db_path, table_name)
    # print()
    # print('--> setup.py', '- Execution time:', secondsToStr(time() - start))
    # print()

    print()
    print('--> setup.py', '- Execution time:', secondsToStr(time() - start))
    print()
