from entities.ContextClassHarvesters import IndividualEntityBuilder as ieb
b = ieb()

with open("logs/import_tests/missing_entities.log", "r") as me:
    for line in me.readlines():
        sline = line.strip()
        b.build_individual_entity(sline)
