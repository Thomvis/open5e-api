import hashlib
import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from api.management.commands.importer import Importer
from api.models import Manifest


def get_hash(filepath):
    # https://stackoverflow.com/a/1131238
    file_hash = hashlib.md5()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()

class Command(BaseCommand):

    help = 'Loads all properly formatted data into the database from the given directories.'
    document = ''

    def add_arguments(self, parser):
        #Positional Arguments.
        parser.add_argument('directories', nargs='+', type=str, help='Directories that contains %model_name%.json files to be loaded.')

        # Named (optional) arguments

        parser.add_argument('--flush', action='store_true', help='Flushes all existing database data before adding new objects.',)

        parser.add_argument('--update', action='store_true', help='Updates existing database data based on slugs.')

        parser.add_argument('--append', action='store_true', help="[Default] Adds new objects if they dont already exist.")

        parser.add_argument('--testrun', action='store_true', help="Do not commit changes.")

    def handle(self, *args, **options):
        directories = options['directories']
        if options['flush']:
            self.stdout.write(self.style.WARNING('Flushing existing database.'))
        elif options['update'] and not options['append']:
            self.stdout.write(self.style.WARNING('Existing matching (by slug) objects are being updated.'))
        elif options['testrun']:
            self.stdout.write(self.style.WARNING('NO CHANGES WILL BE COMMITTED.'))
        elif options['append'] and not options['update']:
            self.stdout.write(self.style.WARNING('Inserting new items into the database. Skipping conflicts (if any).'))
        else:
            raise ValueError('Invalid options combination.')
        self.stdout.write(self.style.SUCCESS(f'Reading in files from {0}'.format(options['directories'])))

        self.options = options

        if bool(options['flush']):
            Manifest.objects.all().delete()

        for directory in options['directories']:
            self._populate_from_directory(Path(directory))

    def _populate_from_directory(self, directory: Path) -> None:
        importer = Importer()
        with open(directory / 'document.json', encoding="utf-8") as doc_data:
            docs = json.load(doc_data)
            self.stdout.write(self.style.SUCCESS(importer.DocumentImporter(self.options, docs)))
        
        bgs_file = Path(directory / 'backgrounds.json')
        if bgs_file.exists():
            bgs_hash = get_hash(bgs_file)
            importer.ManifestImporter(self.options, bgs_file, bgs_hash)
            with open(bgs_file, encoding="utf-8") as bg_data:
                bgs = json.load(bg_data)
                self.stdout.write(self.style.SUCCESS(importer.BackgroundImporter(self.options, bgs)))

        cls_file = Path(directory / 'classes.json')
        if cls_file.exists():
            cls_hash = get_hash(cls_file)
            importer.ManifestImporter(self.options, cls_file, cls_hash)
            with open(cls_file, encoding="utf-8") as cls_data:
                cls = json.load(cls_data)
                self.stdout.write(self.style.SUCCESS(importer.ClassImporter(self.options, cls)))

        con_file = Path(directory / 'conditions.json')
        if con_file.exists():
            con_hash = get_hash(con_file)
            importer.ManifestImporter(self.options, con_file, con_hash)
            with open(con_file, encoding="utf-8") as con_data:
                con = json.load(con_data)
                self.stdout.write(self.style.SUCCESS(importer.ConditionImporter(self.options, con)))

        fea_file = Path(directory / 'feats.json')
        if fea_file.exists():
            fea_hash = get_hash(fea_file)
            importer.ManifestImporter(self.options, fea_file, fea_hash)
            with open(fea_file, encoding="utf-8") as fea_data:
                fea = json.load(fea_data)
                self.stdout.write(self.style.SUCCESS(importer.FeatImporter(self.options, fea)))

        mag_file = Path(directory / 'magicitems.json')
        if mag_file.exists():
            mag_hash = get_hash(mag_file)
            importer.ManifestImporter(self.options, mag_file, mag_hash)
            with open(mag_file, encoding="utf-8") as mag_data:
                mag = json.load(mag_data)
                self.stdout.write(self.style.SUCCESS(importer.MagicItemImporter(self.options, mag)))

        spl_file = Path(directory / 'spells.json')
        if spl_file.exists():
            spl_hash = get_hash(spl_file)
            importer.ManifestImporter(self.options, spl_file, spl_hash)
            with open(spl_file, encoding="utf-8") as spl_data:
                spl = json.load(spl_data)
                self.stdout.write(self.style.SUCCESS(importer.SpellImporter(self.options, spl)))

        mon_file = Path(directory / 'monsters.json')
        if mon_file.exists():
            mon_hash = get_hash(mon_file)
            importer.ManifestImporter(self.options, mon_file, mon_hash)
            with open(mon_file, encoding="utf-8") as mon_data:
                mon = json.load(mon_data)
                self.stdout.write(self.style.SUCCESS(importer.MonsterImporter(self.options, mon)))

        pln_file = Path(directory / 'planes.json')
        if pln_file.exists():
            pln_hash = get_hash(pln_file)
            importer.ManifestImporter(self.options, pln_file, pln_hash)
            with open(pln_file, encoding="utf-8") as pln_data:
                pln = json.load(pln_data)
                self.stdout.write(self.style.SUCCESS(importer.PlaneImporter(self.options, pln)))

        sec_file = Path(directory / 'sections.json')
        if sec_file.exists():
            sec_hash = get_hash(sec_file)
            importer.ManifestImporter(self.options, sec_file, sec_hash)
            with open(sec_file, encoding="utf-8") as sec_data:
                sec = json.load(sec_data)
                self.stdout.write(self.style.SUCCESS(importer.SectionImporter(self.options, sec)))

        rac_file = Path(directory / 'races.json')
        if rac_file.exists():
            rac_hash = get_hash(rac_file)
            importer.ManifestImporter(self.options, rac_file, rac_hash)
            with open(rac_file, encoding="utf-8") as rac_data:
                rac = json.load(rac_data)
                self.stdout.write(self.style.SUCCESS(importer.RaceImporter(self.options, rac)))

        wea_file = Path(directory / 'weapons.json')
        if wea_file.exists():
            wea_hash = get_hash(wea_file)
            importer.ManifestImporter(self.options, wea_file, wea_hash)
            with open(wea_file, encoding="utf-8") as wea_data:
                wea = json.load(wea_data)
                self.stdout.write(self.style.SUCCESS(importer.WeaponImporter(self.options, wea)))

        arm_file = Path(directory / 'armor.json')
        if arm_file.exists():
            with open(arm_file, encoding="utf-8") as arm_data:
                arm = json.load(arm_data)
                self.stdout.write(self.style.SUCCESS(importer.ArmorImporter(self.options, arm)))
