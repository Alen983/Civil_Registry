-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 27, 2020 at 10:10 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `civil`
--

-- --------------------------------------------------------

--
-- Table structure for table `authority`
--

CREATE TABLE IF NOT EXISTS `authority` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `authority` varchar(50) NOT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `authority`
--

INSERT INTO `authority` (`aid`, `authority`) VALUES
(1, 'ElectionCommision'),
(2, 'Registration'),
(3, 'RTO'),
(4, 'passport'),
(5, 'governmentofficial');

-- --------------------------------------------------------

--
-- Table structure for table `authorityapproval`
--

CREATE TABLE IF NOT EXISTS `authorityapproval` (
  `otherid` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL,
  `type` varchar(50) NOT NULL,
  `appdate` date NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`otherid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=18 ;

--
-- Dumping data for table `authorityapproval`
--

INSERT INTO `authorityapproval` (`otherid`, `cid`, `type`, `appdate`, `status`) VALUES
(1, 0, 'licence', '0000-00-00', 'approved'),
(2, 1, 'licence', '2020-02-29', 'approved'),
(3, 1, 'licence', '2020-02-28', 'approved'),
(4, 1, 'passport', '0000-00-00', 'approved'),
(6, 1, 'licence', '2020-02-29', 'approved'),
(7, 6, 'passport', '0000-00-00', 'pending'),
(8, 6, 'passport', '0000-00-00', 'pending'),
(9, 11, 'passport', '0000-00-00', 'approved'),
(10, 14, 'licence', '2020-02-29', 'approved'),
(11, 1, 'licence', '2020-03-27', 'approved'),
(12, 14, 'passport', '0000-00-00', 'approved'),
(13, 17, 'licence', '2020-02-28', 'approved'),
(14, 17, 'licence', '2020-02-29', 'approved'),
(15, 17, 'passport', '0000-00-00', 'approved'),
(16, 17, 'passport', '0000-00-00', 'approved'),
(17, 17, 'licence', '2020-02-28', 'approved');

-- --------------------------------------------------------

--
-- Table structure for table `authorityreg`
--

CREATE TABLE IF NOT EXISTS `authorityreg` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `district` varchar(50) NOT NULL,
  `head` varchar(50) NOT NULL,
  `addr` varchar(50) NOT NULL,
  `phno` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `authorityreg`
--

INSERT INTO `authorityreg` (`aid`, `district`, `head`, `addr`, `phno`, `category`, `username`, `password`) VALUES
(1, 'Ernakulam', 'archana', 'malapuram', '9855423654', 'RTO', 'archana', 'archana'),
(2, 'Kottayam', 'manu', 'skyline', '9854125632', 'Registration', 'manu', 'manu'),
(3, 'Ernakulam', 'ramu', 'kripa', '9875268456', 'Registration', 'ramu', 'ramu'),
(4, 'Kasargod', 'rtyu', 'dertygh', '23456767', 'ElectionCommision', 'rtyu', 'rtyu'),
(5, 'Ernakulam', 'meenu', 'ghfuy', '21345678', 'ElectionCommision', 'meenu', 'meenu'),
(6, 'Ernakulam', 'sanu', 'ddd', '9625412365', 'passport', 'sanu', 'sanu'),
(7, 'Kottayam', 'sfgh', 'fhjg', '7455667788', 'Registration', 'akku', 'akku'),
(8, 'Kottayam', 'sfgh', 'fhjg', '7455667788', 'Registration', 'akku', 'akku'),
(9, 'Kottayam', 'sfgh', 'fhjg', '7455667788', 'Registration', 'akku', 'akku'),
(10, 'Kottayam', 'sdfv', 'nest', '9874526321', 'Registration', 'AKKU', 'OI12345'),
(11, 'Kottayam', 'Aleena', 'dfyg', '7766554488', 'RTO', 'Aleena', 'Aleena');

-- --------------------------------------------------------

--
-- Table structure for table `birthreg`
--

CREATE TABLE IF NOT EXISTS `birthreg` (
  `brid` int(11) NOT NULL AUTO_INCREMENT,
  `dob` date NOT NULL,
  `tob` varchar(50) NOT NULL,
  `dis` varchar(50) NOT NULL,
  `gen` varchar(50) NOT NULL,
  `cname` varchar(50) NOT NULL,
  `mname` varchar(50) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `paddr` varchar(50) NOT NULL,
  `paddrb` varchar(50) NOT NULL,
  `pob` varchar(50) NOT NULL,
  `hosp` varchar(50) NOT NULL,
  `deli` varchar(50) NOT NULL,
  `weight` varchar(50) NOT NULL,
  `dur` varchar(50) NOT NULL,
  `rdate` date NOT NULL,
  `status` varchar(50) NOT NULL,
  `uid` int(11) NOT NULL,
  PRIMARY KEY (`brid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `birthreg`
--

INSERT INTO `birthreg` (`brid`, `dob`, `tob`, `dis`, `gen`, `cname`, `mname`, `fname`, `paddr`, `paddrb`, `pob`, `hosp`, `deli`, `weight`, `dur`, `rdate`, `status`, `uid`) VALUES
(1, '1999-12-03', '0000-00-00', 'ernakulam', 'female', 'ammu', 'pooja', 'anoop', 'dsartdjy', 'agdytfuyt', 'mky', 'rajagiri', 'normal', '3', '2', '1999-12-28', 'forwarded', 1),
(2, '2016-09-25', 'erklmaihhh', 'errkm ', 'female', 'ertadstd', 'gahchah', 'gjchauya', 'ghchayggta', 'tgdausjicga', 'ygadadchuagcf', 'rfdgtt', 'ftatcgtatfcd', 'GAGYCFHg', 'rTDYYU', '2019-09-28', 'forwarded', 2),
(3, '2019-12-11', '12 pm', 'idukki', 'female', 'ponnu', 'pooja', 'anoop', 'green villa', 'green villa', 'mky', 'rajagiri', 'normal', '3', '2', '2019-12-18', 'forwarded', 3),
(4, '1995-12-29', '10 am', 'ernakulam', 'female', 'ammu', 'mariyam', 'sunil', 'oppp', 'pppp', 'hh', 'cochin hospital', 'normal', '2', '2', '2019-12-03', 'forwarded', 2),
(5, '2020-01-14', '2am', 'idukki', 'male', 'Anupama', 'ravi', 'Arya', 'nest, vytilla', 'vytilla', 'ggg', 'rajagiri', 'normal', '2', '2', '2020-01-22', 'forwarded', 11),
(6, '2020-01-15', '2am', 'idukki', 'male', 'arun', 'usha', 'raman', 'aaaaa', 'aaaaa', 'aaaaaaaaaaaa', 'alphonsa', 'normal', '2', '2', '2020-01-21', 'forwarded', 11),
(7, '2020-01-24', '10am', 'ekm', 'female', 'anu', 'anu', 'arun', 'nest, vytilla', 'vytilla', 'ekm', 'Arya', 'normal', '2', '9', '2020-01-15', 'forwarded', 1),
(8, '2020-02-26', '10 am', 'kjh', 'male', 'fyggu', 'sby', 'sjhgyuf', 'ksjhu', 'shui', 'usghu', 'kjsoih', 'normal', '3', '9', '2020-02-29', 'forwarded', 13),
(9, '2020-02-04', '11', 'HG', 'female', 'JG', 'HJF', 'KGF', 'JHG', 'XJJG', 'FGHJ', 'FGHJK', 'normal', '3', '10', '2020-02-28', 'forwarded', 14),
(10, '2020-02-19', '11', 'CVBNM', 'None', 'VAVA', 'VAVA', 'VAVA', 'VAVAVAVA', 'AVAVA', 'VAVA', 'VAVA', '---select method---', '2', '---select Month---', '2020-02-28', 'forwarded', 15);

-- --------------------------------------------------------

--
-- Table structure for table `bride`
--

CREATE TABLE IF NOT EXISTS `bride` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `pic` varchar(500) NOT NULL,
  `nationality` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `occu` varchar(50) NOT NULL,
  `peraddr` varchar(50) NOT NULL,
  `preaddr` varchar(50) NOT NULL,
  `sig` varchar(500) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `fsig` varchar(500) NOT NULL,
  `mname` varchar(50) NOT NULL,
  `msig` varchar(500) NOT NULL,
  `uid` int(11) NOT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `bride`
--

INSERT INTO `bride` (`rid`, `name`, `pic`, `nationality`, `dob`, `occu`, `peraddr`, `preaddr`, `sig`, `fname`, `fsig`, `mname`, `msig`, `uid`) VALUES
(1, 'Riya', '59df21ca16268-3538d65fa23f176ed909f4fef0766047-1200x_.jpg', 'indian', '1999-12-10', 'doctor', 'styughoi', 'trs6ijoijoi', '1.jpg', 'anoop', '1.jpg', 'priya', '1.jpg', 1),
(2, 'anugraha', 'IMG-20190519-WA0000.jpg', 'indian', '2019-09-28', 'dttrrt', 'rtsatgdyyahuschu', 'AFCAEF', 'IMG-20190629-WA0019.jpg', 'GOKUL', 'IMG-20190531-WA0106.jpg', 'SGRR', 'IMG-20190531-WA0114.jpg', 2),
(3, 'meera', 'airplane-wallpaper-3.jpg', 'Indian', '2020-01-06', 'teacher', 'nest', 'flat no 12', 'college_fests.jpg', 'unni', 'NEP2792277.jpg', 'binu', 'Crowd-at-concert6-1600x800.jpg', 1),
(6, 'bini', 'attribcache140.bin', 'Indian', '2020-01-22', 'teacher', 'aaaaa', 'aaaaaaa', 'Class1.cs', 'ramu', 'Class1.cs', 'mini', 'Class1.cs', 11),
(7, 'lijo', 'birthcer.pdf', 'fjfhff', '2020-01-14', 'teacher', 'yui', 'dfghj', 'birthcer.pdf', 'anu', 'birthcer.pdf', 'mini', 'birthcer.pdf', 1),
(8, 'ARYA K S', 'IMG_20171021_152423.jpg', 'Indian', '2021-03-31', 'WHUDT', 'DDDFTH', 'GHFGH', 'photo holic.jpg', 'SIBY MM', 'capture u.jpg', 'SUJA M M', 'IMG_20200210_093127.jpg', 13),
(9, 'ARYA K S', '', 'INDIAN', '2020-01-29', 'WORKING', 'ASERYJF', 'FGJKNLJG', '', 'SIBY M M', '', 'SUJA SIBY', '', 13),
(10, 'GYGY', 'Cyber-Crime-2.jpg-750x430.jpg', 'Indian', '2020-02-18', 'GGVG', 'GVG', 'GG', 'Horticop Management (1)_I4taVE9.docx', 'GGG', 'IMG_20200210_093131.jpg', 'TTGTT', 'kmmgps.sql', 13);

-- --------------------------------------------------------

--
-- Table structure for table `certificatereg`
--

CREATE TABLE IF NOT EXISTS `certificatereg` (
  `certiid` int(11) NOT NULL AUTO_INCREMENT,
  `certificate` varchar(50) NOT NULL,
  `uploadcertificate` varchar(500) NOT NULL,
  `cid` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`certiid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=28 ;

--
-- Dumping data for table `certificatereg`
--

INSERT INTO `certificatereg` (`certiid`, `certificate`, `uploadcertificate`, `cid`, `amount`, `status`) VALUES
(4, 'marriage', '/MEDIA/CIVIL%20REGISTEY_gV3EbJR.html', 1, 200, ''),
(5, 'marriage', '/MEDIA/CIVIL%20REGISTEY_GCubLxy.html', 1, 200, ''),
(6, 'marriage', '/MEDIA/a.jpg', 1, 300, ''),
(7, 'marriage', 'static/MEDIA/a.jpg', 1, 300, ''),
(8, 'marriage', 'static/MEDIA/b.jpg', 1, 200, ''),
(9, 'marriage', 'static/MEDIA/b.jpg', 1, 200, 'paid'),
(10, 'marriage', 'static/MEDIA/CIVIL%20REGISTEY.html', 1, 100, 'paid'),
(11, 'marriage', 'static/MEDIA/birthcer.pdf', 1, 200, ''),
(12, 'Birth', 'static/MEDIA/birthcer_norrRJT.pdf', 1, 100, 'paid'),
(13, 'Birth', 'static/MEDIA/photogrphr.jpg', 1, 200, 'not paid'),
(14, 'birth', 'static/MEDIA/New%20Doc%202019-08-10%2015.37.29.pdf', 1, 200, 'not paid'),
(15, 'Votersid', 'static/MEDIA/Cyber-Crime-Complaint.jpg.jpg', 1, 300, 'not paid'),
(16, 'Votersid', 'static/MEDIA/Cyber-Crime-Complaint.jpg_ss5FQfE.jpg', 3, 100, 'not paid'),
(17, 'Birth', 'static/MEDIA/CATCH%20THE%20CROOK.docx', 1, 200, 'paid'),
(18, 'MARRIAGE', 'static/MEDIA/marriage.pdf', 1, 200, 'not paid'),
(19, 'MARRIAGE', 'static/MEDIA/marriage_dpCqqJs.pdf', 1, 200, 'not paid'),
(20, 'MARRIAGE', 'static/MEDIA/marriage_pYyOABL.pdf', 1, 200, 'not paid'),
(21, 'MARRIAGE', 'static/MEDIA/marriage_I0B7h7g.pdf', 1, 200, 'not paid'),
(22, 'MARRIAGE', 'static/MEDIA/marriage_w1u1oiq.pdf', 13, 200, 'paid'),
(23, 'Birth', 'static/MEDIA/birth.pdf', 13, 400, 'paid'),
(24, 'BIRTH', 'static/MEDIA/B612_20170722_181305_ABhl3td.jpg', 15, 500, 'paid'),
(25, 'Votersid', 'static/MEDIA/vote.pdf', 16, 400, 'not paid'),
(26, 'Votersid', 'static/MEDIA/vote_e2tq1Cc.pdf', 16, 700, 'paid'),
(27, 'Death', 'static/MEDIA/DEATH.pdf', 14, 300, 'paid');

-- --------------------------------------------------------

--
-- Table structure for table `cusreg`
--

CREATE TABLE IF NOT EXISTS `cusreg` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `addr` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `phno` varchar(50) NOT NULL,
  `aadhar` varchar(50) NOT NULL,
  `dob` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=18 ;

--
-- Dumping data for table `cusreg`
--

INSERT INTO `cusreg` (`cid`, `name`, `addr`, `gender`, `phno`, `aadhar`, `dob`, `email`, `username`) VALUES
(1, 'riya', 'dharma', 'female', '9874526354', '2365897452874', '2019-12-11', 'riya@gmail.com', 'riya'),
(2, 'anu', 'anugraha vv viswanth', 'female', '0987766122', '244567657', '2019-08-28', 'anu@gmail.com', 'anu'),
(3, 'merin', 'ariyikattu', 'female', '123456789112', '878346703', '1999-12-11', 'merin@gmail.com', 'merin'),
(11, 'achu', 'green villa', 'female', '9942345678', '456789234567', '2020-01-21', 'achu@gmail.com', 'achu'),
(12, 'megha', 'dfghj', 'female', '9946554894', '635987452632', '2020-02-12', 'megha@gmail.com', 'megha'),
(13, 'ARYA K S', 'kottayam', 'female', '9946554894', '122443211234', '1999-05-17', 'aryaks23417@gmail.com', 'ARYA K S'),
(14, 'UNNI', 'STRDYY', 'female', '7788990077', '565656565656', '2020-02-19', 'HGY@gmail.com', 'UNNI'),
(15, 'VAVA', 'GHJ', 'female', '9988776677', '998877443322', '2020-02-05', 'FGJJ@GMAIL.COM', 'VAVA'),
(16, 'BABY', 'FGHJK', 'female', '6677889900', '436709747863', '2020-02-04', 'DFGHJF2@GMAIL.COM', 'BABY'),
(17, 'amma', 'f', 'female', '9946554894', '554466778899', '2020-02-18', 'fghjk@gmail.com', 'amma');

-- --------------------------------------------------------

--
-- Table structure for table `deathcertificatelegal`
--

CREATE TABLE IF NOT EXISTS `deathcertificatelegal` (
  `did` int(10) NOT NULL AUTO_INCREMENT,
  `dod` date NOT NULL,
  `named` varchar(20) NOT NULL,
  `pad` varchar(20) NOT NULL,
  `gen` varchar(20) NOT NULL,
  `nof` varchar(20) NOT NULL,
  `nom` varchar(20) NOT NULL,
  `addeath` varchar(30) NOT NULL,
  `praddpa` varchar(30) NOT NULL,
  `praddtbirth` varchar(20) NOT NULL,
  `dobdesd` date NOT NULL,
  `pod` varchar(10) NOT NULL,
  `haddrs` varchar(20) NOT NULL,
  `infoname` varchar(20) NOT NULL,
  `inadd` varchar(20) NOT NULL,
  `uid` int(10) NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`did`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `deathcertificatelegal`
--

INSERT INTO `deathcertificatelegal` (`did`, `dod`, `named`, `pad`, `gen`, `nof`, `nom`, `addeath`, `praddpa`, `praddtbirth`, `dobdesd`, `pod`, `haddrs`, `infoname`, `inadd`, `uid`, `status`) VALUES
(8, '2020-01-01', 'cancer', 'riya mathew', 'female', 'mathew', 'mollly', 'nest', 'vytilla', 'mathew john vytila c', '2020-01-23', 'rajagiri', 'nest, vytilla', 'anupama', 'anu', 1, 'forwarded'),
(6, '2020-01-14', 'aa', 'eer', 'male', 'ssds', 'err', 'rr', 'eee', 'eee', '2020-01-15', 'ee', 'ee', 'ee', 'ww', 11, 'forwarded'),
(4, '2020-01-02', 'ron', 'nest', 'male', 'joseph', 'mini', 'nest', 'nest', 'nest', '1987-01-21', 'vytilla', 'nest', 'riya', 'skyline', 1, 'forwarded'),
(7, '2020-01-14', 'manu', 'aaaa', 'male', 'aaaa', 'aaaaa', 'aaaaaaaaaaaaa', 'aaaaa', 'aaaaaa', '2020-01-08', 'aaaa', 'ssss', 'ammu', 'sssss', 11, 'forwarded'),
(9, '2020-02-10', 'ggg', 'ggg', 'male', 'fghj', 'hjk', 'bnm', 'bn', 'vbn', '2019-06-12', 'cvb', 'cvb', 'cvbn', 'cvbn', 14, 'forwarded'),
(10, '2020-02-26', 'VAVA', 'VAVA', 'None', 'VAVA', 'VAVA', 'VAVA', 'VAVA', 'VAVA', '2020-02-06', 'SDFGHJ', 'VBNM,', 'VAVA', 'VAVA', 15, 'forwarded');

-- --------------------------------------------------------

--
-- Table structure for table `deathstatistical`
--

CREATE TABLE IF NOT EXISTS `deathstatistical` (
  `idd` int(10) NOT NULL AUTO_INCREMENT,
  `nod` varchar(20) NOT NULL,
  `noss` varchar(20) NOT NULL,
  `nota` varchar(20) NOT NULL,
  `relg` varchar(30) NOT NULL,
  `tmard` varchar(30) NOT NULL,
  `nd` varchar(20) NOT NULL,
  `medicalcer` varchar(30) NOT NULL,
  `drugsused` varchar(30) NOT NULL,
  `smokeed` varchar(30) NOT NULL,
  `alcoholused` varchar(30) NOT NULL,
  `status` varchar(20) NOT NULL,
  `uid` int(10) NOT NULL,
  PRIMARY KEY (`idd`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `deathstatistical`
--


-- --------------------------------------------------------

--
-- Table structure for table `district`
--

CREATE TABLE IF NOT EXISTS `district` (
  `did` int(11) NOT NULL AUTO_INCREMENT,
  `district` varchar(50) NOT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `district`
--

INSERT INTO `district` (`did`, `district`) VALUES
(1, 'Kasargod'),
(2, 'Kottayam'),
(3, 'Ernakulam'),
(4, 'Kannur');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE IF NOT EXISTS `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `district` varchar(50) NOT NULL,
  `authority` varchar(50) NOT NULL,
  `fb` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `uid` int(11) NOT NULL,
  `reply` varchar(50) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`fid`, `district`, `authority`, `fb`, `date`, `uid`, `reply`) VALUES
(1, 'Ernakulam', 'Registration', 'good', '2019-12-27', 1, ''),
(2, 'Ernakulam', 'RTO', 'bad', '2019-12-28', 1, ''),
(3, 'Ernakulam', 'RTO', 'bad', '2019-12-28', 1, ''),
(4, '', 'RTO', 'bad', '2019-12-29', 3, ''),
(5, 'Kasargod', 'RTO', 'bad', '2019-12-29', 1, 'ok'),
(6, 'Kottayam', 'Registration', 'TERRIBLE', '2020-02-27', 13, '');

-- --------------------------------------------------------

--
-- Table structure for table `forward`
--

CREATE TABLE IF NOT EXISTS `forward` (
  `fwid` int(11) NOT NULL AUTO_INCREMENT,
  `district` varchar(50) NOT NULL,
  `authority` varchar(50) NOT NULL,
  `fdate` date NOT NULL,
  `certid` int(11) NOT NULL,
  `certificate` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`fwid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=61 ;

--
-- Dumping data for table `forward`
--

INSERT INTO `forward` (`fwid`, `district`, `authority`, `fdate`, `certid`, `certificate`, `status`) VALUES
(1, 'Ernakulam', 'Registration', '2019-12-27', 2, 'Marriage', 'forwarded'),
(3, 'Ernakulam', 'Registration', '2019-12-28', 3, 'Marriage', 'forwarded'),
(4, 'Ernakulam', 'Registration', '2019-12-28', 2, 'Marriage', 'forwarded'),
(5, 'Ernakulam', 'Registration', '2019-12-29', 4, 'Marriage', 'forwarded'),
(12, 'Ernakulam', 'Registration', '2019-12-31', 4, 'Birth', 'forwarded'),
(14, 'Ernakulam', 'Rto', '2020-01-05', 4, 'Votersid', 'forwarded'),
(15, 'Ernakulam', 'Registration', '2020-01-05', 5, 'Marriage', 'forwarded'),
(16, 'Ernakulam', 'Registration', '2020-01-15', 3, 'Birth', 'forwarded'),
(17, 'Ernakulam', 'Registration', '2020-01-21', 1, 'Birth', 'forwarded'),
(21, 'Ernakulam', 'Registration', '2020-01-21', 4, 'Death', 'forwarded'),
(22, 'Ernakulam', 'Registration', '2020-01-21', 6, 'Marriage', 'forwarded'),
(23, 'Ernakulam', 'Registration', '2020-01-21', 5, 'Birth', 'forwarded'),
(25, 'Ernakulam', 'Registration', '2020-01-21', 5, 'Death', 'forwarded'),
(26, 'Ernakulam', 'Registration', '2020-01-21', 2, 'Birth', 'forwarded'),
(27, 'Ernakulam', 'Rto', '2020-01-21', 7, 'Votersid', 'forwarded'),
(28, 'Ernakulam', 'Rto', '2020-01-21', 8, 'Votersid', 'forwarded'),
(29, 'Ernakulam', 'Registration', '2020-01-21', 6, 'Death', 'forwarded'),
(30, 'Ernakulam', 'Registration', '2020-01-21', 7, 'Death', 'forwarded'),
(31, 'Ernakulam', 'Registration', '2020-01-21', 6, 'Birth', 'forwarded'),
(32, 'Ernakulam', 'Rto', '2020-01-21', 9, 'Votersid', 'forwarded'),
(33, 'Ernakulam', 'Rto', '2020-01-21', 6, 'Votersid', 'forwarded'),
(34, 'Ernakulam', 'Registration', '2020-01-25', 7, 'Birth', 'forwarded'),
(35, 'Ernakulam', 'Registration', '2020-01-25', 8, 'Death', 'forwarded'),
(37, 'Ernakulam', 'Rto', '2020-02-23', 2, 'Licence', 'forwarded'),
(38, 'Ernakulam', 'Rto', '2020-02-23', 3, 'Licence', 'forwarded'),
(39, 'Ernakulam', 'passport', '2020-02-24', 1, 'passport', 'forwarded'),
(40, 'Ernakulam', 'passport', '2020-02-24', 1, 'passport', 'forwarded'),
(41, 'Ernakulam', 'Rto', '2020-02-25', 4, 'Licence', 'forwarded'),
(42, 'Ernakulam', 'passport', '2020-02-27', 3, 'passport', 'forwarded'),
(43, 'Ernakulam', 'passport', '2020-02-27', 2, 'passport', 'forwarded'),
(44, 'Ernakulam', 'passport', '2020-02-27', 4, 'passport', 'forwarded'),
(45, 'Ernakulam', 'Registration', '2020-02-27', 10, 'Marriage', 'forwarded'),
(46, 'Ernakulam', 'Registration', '2020-02-27', 8, 'Birth', 'forwarded'),
(47, 'Ernakulam', 'ElectionCommision', '2020-02-27', 11, 'Votersid', 'forwarded'),
(48, 'Ernakulam', 'Rto', '2020-02-27', 5, 'Licence', 'forwarded'),
(49, 'Ernakulam', 'Rto', '2020-02-27', 1, 'Licence', 'forwarded'),
(50, 'Ernakulam', 'passport', '2020-02-27', 5, 'passport', 'forwarded'),
(51, 'Ernakulam', 'Registration', '2020-02-27', 9, 'Death', 'forwarded'),
(52, 'Ernakulam', 'Registration', '2020-02-27', 9, 'Birth', 'forwarded'),
(53, 'Ernakulam', 'Registration', '2020-02-27', 10, 'Birth', 'forwarded'),
(54, 'Ernakulam', 'Registration', '2020-02-27', 10, 'Death', 'forwarded'),
(55, 'Ernakulam', 'ElectionCommision', '2020-02-27', 12, 'Votersid', 'forwarded'),
(56, 'Ernakulam', 'Rto', '2020-02-27', 6, 'Licence', 'forwarded'),
(57, 'Ernakulam', 'Rto', '2020-02-27', 7, 'Licence', 'forwarded'),
(58, 'Ernakulam', 'passport', '2020-02-27', 6, 'passport', 'forwarded'),
(59, 'Ernakulam', 'passport', '2020-02-27', 7, 'passport', 'forwarded'),
(60, 'Ernakulam', 'Rto', '2020-02-27', 8, 'Licence', 'forwarded');

-- --------------------------------------------------------

--
-- Table structure for table `groom`
--

CREATE TABLE IF NOT EXISTS `groom` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `pic` varchar(500) NOT NULL,
  `nationality` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `occu` varchar(50) NOT NULL,
  `peraddr` varchar(50) NOT NULL,
  `preaddr` varchar(50) NOT NULL,
  `sig` varchar(500) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `fsig` varchar(500) NOT NULL,
  `mname` varchar(50) NOT NULL,
  `msig` varchar(500) NOT NULL,
  `uid` int(11) NOT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `groom`
--

INSERT INTO `groom` (`rid`, `name`, `pic`, `nationality`, `dob`, `occu`, `peraddr`, `preaddr`, `sig`, `fname`, `fsig`, `mname`, `msig`, `uid`) VALUES
(1, 'Vinod', '1.jpg', 'indian', '1998-12-02', 'doctor', 'eruio87', 'yryio', '59df21ca16268-3538d65fa23f176ed909f4fef0766047-1200x_.jpg', 'nayar', '59df21ca16268-3538d65fa23f176ed909f4fef0766047-1200x_.jpg', 'ammu', '1.jpg', 1),
(2, 'gokul', 'IMG_20190525_094902.jpg', 'indian', '2019-11-28', 'doctor', 'ygcfyhuasucdh', 'DAFAF', 'IMG-20190531-WA0116.jpg', 'ANU', 'IMG-20190531-WA0113.jpg', 'SREFAGS', 'IMG-20190531-WA0115.jpg', 2),
(3, 'gopan', 'airplane-wallpaper-1.jpg', 'Indian', '2019-12-31', 'engineer', 'nest', 'flat no 12', 'front_pic.jpg', 'vinu', 'IMG_20171211_085439.jpg', 'binil', 'minions_2015_cartoon_100453_1920x1080.jpg', 1),
(6, 'binu', 'Class1.cs', 'Indian', '2020-01-14', 'engineer', 'ssssss', 'ssssssss', 'Class1.cs', 'raghav', 'Class1.cs', 'binil', 'Class1.cs', 11),
(7, 'hh', 'birthcer.pdf', 'tryujk', '2020-01-15', 'engineer', 'tyui', 'dfghj', 'birthcer.pdf', 'anu', 'birthcer.pdf', 'binil', 'birthcer.pdf', 1),
(8, 'APPU H', 'IMG_20200210_093131.jpg', 'Indian', '2023-12-31', 'DWEDE', 'FHJUDGV', 'HJKI', 'cap img3.jpg', 'SANTHOSH H', 'IMG_20200210_093131.jpg', 'SANDHYA E K J', 'IMG_20200122_171640_HDR.jpg', 13),
(9, 'KARTHIK S', '', 'INDIAN', '0000-00-00', 'WORKING', 'AERKMBCG', 'KOITJHVJ', '', 'SANTHOSH K', '', 'SNDHYA', '', 13),
(10, 'YGY', 'shadow.jpg', 'Indian', '2020-02-25', 'GG', 'GG', 'GGG', 'Horticop Management (1)_I4taVE9.docx', 'GBBGB', 'IMG_20200210_093131.jpg', 'bgbg', 'IMG_20200210_093127.jpg', 13);

-- --------------------------------------------------------

--
-- Table structure for table `licencereg`
--

CREATE TABLE IF NOT EXISTS `licencereg` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `licencenum` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `district` varchar(50) NOT NULL,
  `taluk` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phno` varchar(50) NOT NULL,
  `addr` varchar(50) NOT NULL,
  `idproof` varchar(200) NOT NULL,
  `addrproof` varchar(200) NOT NULL,
  `ageproof` varchar(200) NOT NULL,
  `pic` varchar(200) NOT NULL,
  `sig` varchar(200) NOT NULL,
  `appointment` date NOT NULL,
  `cid` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `licencereg`
--

INSERT INTO `licencereg` (`lid`, `licencenum`, `name`, `dob`, `district`, `taluk`, `email`, `phno`, `addr`, `idproof`, `addrproof`, `ageproof`, `pic`, `sig`, `appointment`, `cid`, `status`) VALUES
(1, '3456789', 'archana', '2020-02-05', 'ernakulam', 'ttt', 'arch@gmail.com', '9856325415', 'ddd', 'shutterstock_150468989.jpg', 'Horticop Management (1).docx', 'Horticop Management (1).docx', 'shutterstock_150468989.jpg', 'Computer-Forensic-630x421.jpg', '2020-03-27', 1, 'forwarded'),
(2, '345667', 'mm', '2020-02-03', 'ernakulam', 'vathikudy', 'jin@gmail.com', '9987654323', 'aaaaaaaaaaaaaaaaa', 'static/MEDIA/Horticop%20Management%20(1).docx', 'static/MEDIA/Horticop%20Management%20(1)_hb4Sd1D.docx', 'static/MEDIA/Horticop%20Management%20(1)_3VbSyH8.docx', 'static/MEDIA/Horticop%20Management%20(1)_cZ9giY6.docx', 'static/MEDIA/Horticop%20Management%20(1)_I4taVE9.docx', '2020-02-29', 1, 'forwarded'),
(3, '7689', 'pp', '2020-02-19', 'ernakulam', 'vathikudy', 'ui@gmail.com', '9685745213', 'yui', 'static/MEDIA/cap%20img3.jpg', 'static/MEDIA/cap%20img2.jpeg', 'static/MEDIA/cap%20img2_ux8D8OF.jpeg', 'static/MEDIA/cap%20img3_SvAo90J.jpg', 'static/MEDIA/cap%20img3_MzX0UaY.jpg', '2020-02-29', 1, 'forwarded'),
(4, '256987', 'ananthu', '2020-02-04', 'ernakulam', 'vathikudy', 'ananthu@gmail.com', '9652365412', 'ggg', 'static/MEDIA/shutterstock_150468989.jpg', 'static/MEDIA/shutterstock_150468989_qDxJmdN.jpg', 'static/MEDIA/shutterstock_150468989_gFsXvCp.jpg', 'static/MEDIA/shutterstock_150468989_nvCNdHc.jpg', 'static/MEDIA/shutterstock_150468989_1e3oG1q.jpg', '2020-02-29', 1, 'forwarded'),
(5, '123', 'wdgfr', '2020-02-25', 'ernakulam', 'vathikudy', 'anb@gmail.com', '8877660099', 'fdy', 'static/MEDIA/20161223_154346-1.jpg', 'static/MEDIA/_20161015_171840.jpg', 'static/MEDIA/_20170122_152758.jpg', 'static/MEDIA/2016-04-14-17-12-33-983.jpg', 'static/MEDIA/img_20150429_130142264.jpg', '2020-02-29', 14, 'forwarded'),
(6, 'f55', 'amma', '2020-02-04', 'fgj', 'fghjk', 'ghjk@gmail.com', '6677889900', 'fghjk', 'static/MEDIA/_20161015_171840_hRlq04v.jpg', 'static/MEDIA/_20161010_202745_sWZ8DFL.jpg', 'static/MEDIA/_20170424_190853.jpg', 'static/MEDIA/2016-04-14-17-12-33-983_cOZOEut.jpg', 'static/MEDIA/_20170403_201016.jpg', '2020-02-28', 17, 'forwarded'),
(7, '434', 'dddd', '2020-02-11', 'df', 'fghjk', 'asf@hmail.com', '9988778899', 'fgj', 'static/MEDIA/_20161010_202745_arkwJxe.jpg', 'static/MEDIA/_20161010_202745_ejHGk27.jpg', 'static/MEDIA/_20161015_171840_CZugIa8.jpg', 'static/MEDIA/_20170122_152758_7fs8g2v.jpg', 'static/MEDIA/_20170424_190337.jpg', '2020-02-29', 17, 'forwarded'),
(8, '324', 'amma', '2020-02-19', 'sdfghj', 'sdfghj', 'sdfgh@gmail.com', '9988776655', 'asdfghjk', 'static/MEDIA/IMG_20200210_093131_KkxMLy3.jpg', 'static/MEDIA/IMG_20200210_093131_ex65G5E.jpg', 'static/MEDIA/IMG_20200210_093131_k0RRkMp.jpg', 'static/MEDIA/IMG_20200210_093131_0b8ehmT.jpg', 'static/MEDIA/IMG_20200210_093131_E01u5QO.jpg', '2020-02-28', 17, 'forwarded');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`, `type`) VALUES
('manu', 'manu', 'Registration'),
('riya', 'riya', 'customer'),
('admin', 'admin', 'admin'),
('ramu', 'ramu', 'Registration'),
('anu', 'anu', 'customer'),
('merin', 'merin', 'customer'),
('rtyu', 'rtyu', 'ElectionCommision'),
('meenu', 'meenu', 'ElectionCommision'),
('achu', 'achu', 'customer'),
('megha', 'megha123', 'customer'),
('archana', 'archana', 'RTO'),
('sanu', 'sanu', 'passport'),
('ARYA K S', 'ARYAKS', 'customer'),
('akku', 'akku', 'Registration'),
('akku', 'akku', 'Registration'),
('akku', 'akku', 'Registration'),
('AKKU', 'OI12345', 'Registration'),
('UNNI', 'UNNIUNNI', 'customer'),
('Aleena', 'Aleena', 'RTO'),
('VAVA', 'VAVAVAVA', 'customer'),
('BABY', 'BABYBABY', 'customer'),
('amma', 'ammaamma', 'customer');

-- --------------------------------------------------------

--
-- Table structure for table `marriageregistration`
--

CREATE TABLE IF NOT EXISTS `marriageregistration` (
  `mid` int(11) NOT NULL AUTO_INCREMENT,
  `dom` date NOT NULL,
  `pom` varchar(50) NOT NULL,
  `localarea` varchar(50) NOT NULL,
  `village` varchar(50) NOT NULL,
  `taluk` varchar(50) NOT NULL,
  `dist` varchar(50) NOT NULL,
  `mstatus` varchar(50) NOT NULL,
  `uid` int(11) NOT NULL,
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `marriageregistration`
--

INSERT INTO `marriageregistration` (`mid`, `dom`, `pom`, `localarea`, `village`, `taluk`, `dist`, `mstatus`, `uid`) VALUES
(1, '2019-12-09', 'hall', 'vytilla', 'elamkunnapuzha', 'paravur', 'ernakulam', '1', 0),
(2, '2019-12-03', 'ernakulam', 'vytilla', 'elamkunnapuzha', 'paravur', 'ernakulam', 'forwarded', 1),
(3, '2020-01-06', 'vytilla', 'mm', 'kochi', 'kochi', 'ernakulam', 'forwarded', 1),
(6, '2020-01-22', 'mky', 'mky', 'vathikudy', 'idukki', 'idukki', 'forwarded', 11),
(7, '2020-01-14', 'aluv', 'gg', 'hh', 'hh', 'hh', 'applied', 1),
(8, '2020-02-02', 'KOTTAYAM', 'NAGAMPADOM', 'PANACHIKKAD', 'KOTTAYAM', 'KOTTAYAM', 'applied', 13),
(9, '2020-02-12', 'kottayam', 'nagambadom', 'panachikkad', 'kottayam', 'kottayam', 'applied', 13),
(10, '2020-02-19', 'EFARA', 'GYG', 'BHHB', 'HBH', 'HB', 'forwarded', 13);

-- --------------------------------------------------------

--
-- Table structure for table `passport`
--

CREATE TABLE IF NOT EXISTS `passport` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `district` varchar(50) NOT NULL,
  `taluk` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phno` varchar(50) NOT NULL,
  `addr` varchar(50) NOT NULL,
  `qualification` varchar(50) NOT NULL,
  `emptype` varchar(50) NOT NULL,
  `idproof` varchar(200) NOT NULL,
  `addrproof` varchar(200) NOT NULL,
  `ageproof` varchar(200) NOT NULL,
  `pic` varchar(200) NOT NULL,
  `sig` varchar(200) NOT NULL,
  `cid` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `passport`
--

INSERT INTO `passport` (`lid`, `name`, `dob`, `district`, `taluk`, `email`, `phno`, `addr`, `qualification`, `emptype`, `idproof`, `addrproof`, `ageproof`, `pic`, `sig`, `cid`, `status`) VALUES
(1, 'magha', '2020-02-04', 'ernakulam', 'vathikudy', 'motta@gmail.com', '9874526326', 'aaaa', 'degree', 'student', 'static/MEDIA/gps_60U6PXx.jpg', 'static/MEDIA/gps_3R7CF8z.jpg', 'static/MEDIA/gps_hY4AQYz.jpg', 'static/MEDIA/gps_rd0UMtz.jpg', 'static/MEDIA/gps_D5jQrfv.jpg', 1, 'forwarded'),
(2, 'niya', '2020-02-18', 'ernakulam', 'vathikudy', 'niya@gmail.com', '9658745263', 'fghjk', 'degree', 'student', 'static/MEDIA/professional-photographer.jpg', 'static/MEDIA/photo%20holic.jpg', 'static/MEDIA/professional-photographer_iPxegpe.jpg', 'static/MEDIA/professional-photographer_mG2pebj.jpg', 'static/MEDIA/professional-photographer_LlnNshR.jpg', 1, 'forwarded'),
(3, 'achu', '2020-02-12', 'ernakulam', 'vathikudy', 'achu@gmail.com', '9854755263', 'dfgh', 'degree', 'student', 'static/MEDIA/shutterstock_150468989.jpg', 'static/MEDIA/shutterstock_150468989_8KjWVl5.jpg', 'static/MEDIA/shutterstock_150468989_KQQBGHb.jpg', 'static/MEDIA/shutterstock_150468989_U7yUUvo.jpg', 'static/MEDIA/shutterstock_150468989_9iEyiVx.jpg', 11, 'forwarded'),
(4, 'ben', '2020-02-12', 'ernakulam', 'vathikudy', 'ben@gmail.com', '8546325698', 'ghjk', 'degree', 'student', 'static/MEDIA/CATCH%20THE%20CROOK_9JNzodm.docx', 'static/MEDIA/Horticop%20Management%20(1)_I4taVE9_UFSyiiW.docx', 'static/MEDIA/shutterstock_150468989_kG6qKMD.jpg', 'static/MEDIA/shutterstock_150468989_yHlNdu8.jpg', 'static/MEDIA/shutterstock_150468989_NsQEJ2x.jpg', 11, 'forwarded'),
(5, 'anuja', '2020-02-24', 'JHF', 'RTI', 'anu@gmail.com', '9987654345', 'aaaa', 'bsc', 'uytrf', 'static/MEDIA/IMG_20170713_172818620.jpg', 'static/MEDIA/B612_20170722_181305.jpg', 'static/MEDIA/B612_20170722_181652.jpg', 'static/MEDIA/B612_20170722_160633.jpg', 'static/MEDIA/B612_20170722_182005.jpg', 14, 'forwarded'),
(6, 'anu', '2020-02-26', 'dfgh', 'ghjk', 'arya@gmail.com', '9874526321', 'nest', 'sslc', '234', 'static/MEDIA/_20170403_201016_eSK0ZNP.jpg', 'static/MEDIA/xl-2016-cybercrime-1.jpg', 'static/MEDIA/civil%20(17).sql', 'static/MEDIA/IMG_20200210_093131.jpg', 'static/MEDIA/Senior%20care%20services.docx', 17, 'forwarded'),
(7, 'amma', '2020-02-26', 'dfghj', 'dfghj', 'ae@gmail.com', '9946554894', 'asdfghj', 'others', 'ghj', 'static/MEDIA/IMG_20200210_093131_GOuyUVT.jpg', 'static/MEDIA/IMG_20200210_093131_pHJKQTr.jpg', 'static/MEDIA/IMG_20200210_093131_X31FS5Y.jpg', 'static/MEDIA/IMG_20200210_093131_Tl9eGLN.jpg', 'static/MEDIA/IMG_20200210_093127.jpg', 17, 'forwarded');

-- --------------------------------------------------------

--
-- Table structure for table `rationreg`
--

CREATE TABLE IF NOT EXISTS `rationreg` (
  `rcid` int(11) NOT NULL AUTO_INCREMENT,
  `taluk` date NOT NULL,
  `headname` varchar(50) NOT NULL,
  `pic` varchar(200) NOT NULL,
  `muncipality` varchar(50) NOT NULL,
  `wardnum` varchar(50) NOT NULL,
  `hnum` varchar(50) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `paddrb` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `village` varchar(50) NOT NULL,
  `pincode` varchar(50) NOT NULL,
  `phonenum` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `uid` int(11) NOT NULL,
  PRIMARY KEY (`rcid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `rationreg`
--


-- --------------------------------------------------------

--
-- Table structure for table `votersid`
--

CREATE TABLE IF NOT EXISTS `votersid` (
  `vid` int(11) NOT NULL AUTO_INCREMENT,
  `district` varchar(50) NOT NULL,
  `applicant` varchar(50) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `age` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(50) NOT NULL,
  `hname` varchar(50) NOT NULL,
  `street` varchar(50) NOT NULL,
  `town` varchar(50) NOT NULL,
  `po` varchar(50) NOT NULL,
  `pincode` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phno` varchar(50) NOT NULL,
  `pic` varchar(300) NOT NULL,
  `ageproof` varchar(50) NOT NULL,
  `addrproof` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `uid` int(11) NOT NULL,
  PRIMARY KEY (`vid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `votersid`
--

INSERT INTO `votersid` (`vid`, `district`, `applicant`, `fname`, `age`, `dob`, `gender`, `hname`, `street`, `town`, `po`, `pincode`, `email`, `phno`, `pic`, `ageproof`, `addrproof`, `status`, `uid`) VALUES
(4, 'Ernakulam', 'Arya', 'sdfs', '25', '2020-01-07', 'None', 'nest', 'vytilla', 'ggg', 'fghj', '685259', 'arya@gmail.com', '09685745213', 'static/MEDIA/Boeing_777_Saudi_Arabian_Airlines-1920x1080-660x371.jpg', 'None', 'None', 'forwarded', 3),
(5, 'Ernakulam', 'motta', 'aaa', '22', '2020-01-22', 'None', 'aaaa', 'ssss', 'ddddd', 'fffff', '987654rerdf', 'motta@gmail.com', '456788899', 'static/MEDIA/Class1.cs', 'None', 'None', 'forwarded', 11),
(6, 'Ernakulam', 'motta', 'aaa', '22', '2020-01-22', 'None', 'aaaa', 'ssss', 'ddddd', 'fffff', '987654rerdf', 'motta@gmail.com', '4567888994677', 'static/MEDIA/Class1_RaY15PU.cs', 'None', 'None', 'forwarded', 11),
(7, 'Ernakulam', 'motta', 'aaa', '22', '2020-01-22', 'None', 'aaaa', 'ssss', 'ddddd', 'fffff', '987654rerdf', 'motta@gmail.com', '4567888994677', 'static/MEDIA/Class1_V5IappF.cs', 'None', 'None', 'forwarded', 11),
(8, 'idukki', 'anuja', 'nirmal', '20', '2020-01-14', 'None', 'aaaa', 'sssssss', 'dddddd', 'sssssssssss', '987654', 'anu@gmail.com', '9987654345', 'static/MEDIA/Class1_jFvwMLz.cs', 'None', 'None', 'forwarded', 1),
(9, 'Ernakulam', 'achu', 'aaaaaaaaaa', '45', '2020-01-15', 'None', 'aaaaaaaaaaaaaaaaa', 'sssssssssssssss', 'sssssssssssss', 'ssssssssssss', '876543', 'a@gmail.com', '9987654323', 'static/MEDIA/Class1_XGyCFrL.cs', 'None', 'None', 'forwarded', 11),
(10, 'Ernakulam', 'anu', 'arun', '40', '2020-01-22', 'None', 'nest', 'vytilla', 'ekm', 'ekm', '685259', 'arya@gmail.com', '9874526321', 'static/MEDIA/capture.jpg', 'None', 'None', 'applied', 1),
(11, 'DFGBH', 'YHTRH', 'UEHYU', '30', '1989-05-17', 'male', 'RETGRE', 'FGHYU', 'IUYKOIY', 'YUVK', '686098', 'ARYA@GMAIL.COM', '8877665544', 'static/MEDIA/_20161010_202745.jpg', 'None', 'None', 'forwarded', 14),
(12, 'CVB', 'BABY', 'BABY', '23', '2020-02-13', 'None', 'DFGHJ', 'FGHJ', 'C', 'VBN', '454545', 'WER@GMAIL.COM', '7878095423', 'static/MEDIA/B612_20170722_182005_pScmQFZ.jpg', 'None', 'None', 'forwarded', 16);

-- --------------------------------------------------------

--
-- Table structure for table `witness`
--

CREATE TABLE IF NOT EXISTS `witness` (
  `wid` int(11) NOT NULL AUTO_INCREMENT,
  `mcertid` int(11) NOT NULL,
  `wname` varchar(50) NOT NULL,
  `waddr` varchar(50) NOT NULL,
  `wsign` varchar(300) NOT NULL,
  PRIMARY KEY (`wid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=17 ;

--
-- Dumping data for table `witness`
--

INSERT INTO `witness` (`wid`, `mcertid`, `wname`, `waddr`, `wsign`) VALUES
(1, 123, 'ase', 'green villa', 'None'),
(2, 1223, 'pooja', 'rosevillla', 'None'),
(3, 12, 'ANU', 'GVSXHH', 'None'),
(4, 12, 'AGHG', 'DFF', 'None'),
(5, 245, 'bony', 'hhh', 'None'),
(6, 246, 'tony', 'kkk', 'None'),
(7, 2, 'ammu', 'wwwww', 'None'),
(8, 5, 'anu', 'qqqqqqq', 'None'),
(9, 2451, 'anu', 'nest', 'None'),
(10, 2452, 'anu', 'nest, vytilla', 'None'),
(11, 123, 'POOJA S', 'HHHXYUSFHJ', 'None'),
(12, 1234, 'ARYA H', 'HGFJ', 'None'),
(13, 123, 'POOJA', 'FJFV', 'None'),
(14, 1234, 'AKKU', 'HDGH', 'None'),
(15, 45, 'ttf', 'fcdc', 'None'),
(16, 67, 'fft', 'ffcf', 'None');
