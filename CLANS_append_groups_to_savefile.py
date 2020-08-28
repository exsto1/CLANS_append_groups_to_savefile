import argparse
import os

parser = argparse.ArgumentParser(
    description="Append groups to CLANS savefile. More info can be found in README file.")

parser.add_argument("-c", "--clans", help="path to CLANS savefile. WARNING: old groups will be ignored")
parser.add_argument("-g", "--groups", help="path to folder with group files. More info in README")
parser.add_argument("-o", "--output", help="output file name", default="new_CLANS_savefile")
parser.add_argument("-d", "--dot", help="default dot size for all unspecified groups", default="5")

args = parser.parse_args()

CLANS_savefile = os.path.abspath(args.clans)
output_file = os.path.abspath(args.output)
dot_size = args.dot
groups_folder = os.path.abspath(args.groups)


CLANS = open(CLANS_savefile).read()

intro = CLANS.split(r"</seq>")[0]
outro = CLANS.split(r"</seq>")[1]

sequences = CLANS.split("<seq>")[1].split(r"</seq>")[0].split("\n")
sequences = [i.lstrip(">") for i in sequences if ">" in i]

groups = []
for file in os.listdir(groups_folder):
    group_file = open("%s/%s" % (groups_folder, file)).readlines()
    group_file = [i.rstrip() for i in group_file]

    groupname = os.path.splitext(file)[0]
    groupname = os.path.basename(groupname)
    size = dot_size
    hide = "0"
    color = "255;0;0;255"

    if "# CONFIG:" in group_file[0]:
        options = group_file[0].split("# CONFIG:")[1].split(",")
        options = {i.split("=")[0]: i.split("=")[1] for i in options if i}
        if "name" in options:
            groupname = options["name"]
        if "size" in options:
            size = options["size"]
        if "hide" in options:
            hide = options["hide"]
        if "color" in options:
            color = options["color"]

    temp = "name=%s\ntype=0\nsize=%s\nhide=%s\ncolor=%s\nnumbers=" % (groupname, size, hide, color)

    seq_index = []
    for name in range(len(group_file)):
        if "#" not in group_file[name]:
            if group_file[name] in sequences:
                seq_index.append(str(sequences.index(group_file[name])))
            else:
                print("Invalid name %s: %s - file %s" % (name, group_file[name], file))
    temp += ";".join(seq_index) + ";"
    groups.append(temp)


out = open(output_file, "w")

out.write(intro)
out.write("</seq>\n<seqgroups>\n")
out.write("\n".join(groups))
out.write("\n</seqgroups>")
out.write(outro)

out.close()


# CONFIG line example
"""
# CONFIG:name=XXX,size=XXX,hide=X,color=XXX;XXX;XXX;XXX
"""

# Group example in CLANS savefile
"""
name=SMALL
type=0
size=4
hide=0
color=255;0;0;255
numbers=1704;1703;1702;1701;1700;1699;1698;1695;1693;1691;1690;1684;1681;1676;1675;1674;1673;1672;1670;1669;1664;1663;1657;1656;1653;1652;1651;1650;1647;1645;1644;1643;1642;1640;1638;1635;1630;1629;1628;1627;1624;1622;1615;1614;1613;1611;1609;1601;1599;1598;1597;1595;1591;1588;1587;1585;1584;1580;1579;1578;1573;1570;1567;1561;1558;1552;1545;1544;1543;1539;1536;1534;1533;1532;1531;1530;1529;1527;1522;1521;1518;1513;1509;1506;1503;1502;1499;1498;1496;1495;1493;1489;1488;1484;1482;1481;1480;1479;1475;1473;1471;1469;1465;1462;1459;1457;1453;1452;1445;1443;1440;1438;1435;1434;1432;1429;1427;1420;1416;1414;1408;1405;1403;1402;1401;1397;1396;1394;1390;1389;1382;1379;1377;1374;1373;1369;1368;1360;1355;1354;1353;1352;1348;1347;1346;1344;1343;1342;1339;1335;1334;1333;1328;1327;1326;1321;1317;1314;1313;1310;1309;1305;1304;1302;1297;1295;1292;1288;1286;1283;1282;1281;1280;1277;1275;1274;1269;1266;1265;1261;1258;1255;1248;1247;1246;1245;1242;1241;1240;1239;1237;1235;1233;1232;1227;1224;1221;1216;1215;1214;1210;1209;1207;1198;1197;1195;1190;1185;1182;1181;1180;1179;1178;1173;1171;1169;1167;1166;1164;1163;1161;1160;1157;1153;1149;1148;1147;1145;1144;1143;1135;1129;1126;1125;1124;1120;1119;1115;1113;1112;1111;1107;1105;1103;1102;1099;1098;1095;1092;1087;1083;1081;1080;1077;1075;1073;1068;1060;1059;1058;1050;1049;1047;1039;1036;1035;1025;1023;1021;1017;1015;1012;1011;1005;1004;1003;999;997;995;994;992;990;987;986;983;982;980;979;978;976;975;969;967;962;961;954;952;946;945;943;941;940;937;936;935;930;927;924;920;919;917;915;914;912;911;907;906;904;902;901;900;897;894;893;888;884;877;876;874;869;867;860;858;857;854;849;847;845;840;836;834;830;825;822;820;819;815;814;810;809;808;807;806;805;804;803;801;800;794;791;789;785;784;783;782;780;778;774;773;764;762;760;752;751;749;746;745;744;743;741;740;739;731;728;723;722;721;719;718;715;714;712;710;709;708;706;705;702;698;695;692;691;690;689;687;685;681;679;676;675;674;673;672;668;667;666;662;660;659;655;653;652;647;645;643;638;637;633;631;629;628;626;624;623;620;610;607;605;604;603;598;590;583;582;574;571;569;567;565;562;561;557;550;546;545;543;539;534;532;531;529;527;523;521;519;518;513;512;509;507;506;502;500;497;495;493;492;489;488;486;485;483;481;476;474;473;469;466;465;463;461;459;456;455;452;451;449;448;439;438;437;433;432;431;430;428;424;422;420;415;411;388;386;385;384;382;381;380;378;375;372;371;368;364;362;361;357;356;355;353;352;351;348;342;339;336;334;333;332;330;325;324;316;315;312;309;308;305;303;302;291;289;286;283;282;281;279;277;276;267;263;255;252;247;242;241;239;234;232;229;228;227;225;224;223;216;210;206;203;200;198;197;195;191;189;188;186;184;181;180;175;173;172;170;168;162;161;158;157;156;152;151;149;146;145;143;142;137;129;124;120;117;115;114;112;108;104;100;95;94;92;83;82;79;73;62;59;56;55;47;37;34;33;21;20;13;12;10;5;0;
"""




