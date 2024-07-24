#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v17
# autospec commit: b5caddc
#
Name     : R-nanoparquet
Version  : 0.3.1
Release  : 1
URL      : https://cran.r-project.org/src/contrib/nanoparquet_0.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/nanoparquet_0.3.1.tar.gz
Summary  : Read and Write 'Parquet' Files
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: R-nanoparquet-lib = %{version}-%{release}
Requires: R-nanoparquet-license = %{version}-%{release}
BuildRequires : R-bit64
BuildRequires : R-duckdb
BuildRequires : R-hms
BuildRequires : R-mockery
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Can read most 'Parquet' data types. Can write many 'R' data types,
    including factors and temporal types. See docs for limitations.

%package lib
Summary: lib components for the R-nanoparquet package.
Group: Libraries
Requires: R-nanoparquet-license = %{version}-%{release}

%description lib
lib components for the R-nanoparquet package.


%package license
Summary: license components for the R-nanoparquet package.
Group: Default

%description license
license components for the R-nanoparquet package.


%prep
%setup -q -n nanoparquet

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1721843555

%install
export SOURCE_DATE_EPOCH=1721843555
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-nanoparquet
cp %{_builddir}/nanoparquet/src/fastpforlib/LICENSE %{buildroot}/usr/share/package-licenses/R-nanoparquet/34774a54e4b286739f317922b31ba5eb3ec9195e || :
cp %{_builddir}/nanoparquet/src/miniz/LICENSE %{buildroot}/usr/share/package-licenses/R-nanoparquet/7d3772817ef6dd00f95c6841e07552968eb74600 || :
cp %{_builddir}/nanoparquet/src/zstd/LICENSE %{buildroot}/usr/share/package-licenses/R-nanoparquet/f39758dda00281db4eefbe95ee61c3cc225c7102 || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/nanoparquet/COPYRIGHTS
/usr/lib64/R/library/nanoparquet/DESCRIPTION
/usr/lib64/R/library/nanoparquet/INDEX
/usr/lib64/R/library/nanoparquet/LICENSE
/usr/lib64/R/library/nanoparquet/Meta/Rd.rds
/usr/lib64/R/library/nanoparquet/Meta/features.rds
/usr/lib64/R/library/nanoparquet/Meta/hsearch.rds
/usr/lib64/R/library/nanoparquet/Meta/links.rds
/usr/lib64/R/library/nanoparquet/Meta/nsInfo.rds
/usr/lib64/R/library/nanoparquet/Meta/package.rds
/usr/lib64/R/library/nanoparquet/NAMESPACE
/usr/lib64/R/library/nanoparquet/NEWS.md
/usr/lib64/R/library/nanoparquet/R/nanoparquet
/usr/lib64/R/library/nanoparquet/R/nanoparquet.rdb
/usr/lib64/R/library/nanoparquet/R/nanoparquet.rdx
/usr/lib64/R/library/nanoparquet/WORDLIST
/usr/lib64/R/library/nanoparquet/extdata/userdata1.parquet
/usr/lib64/R/library/nanoparquet/help/AnIndex
/usr/lib64/R/library/nanoparquet/help/aliases.rds
/usr/lib64/R/library/nanoparquet/help/nanoparquet.rdb
/usr/lib64/R/library/nanoparquet/help/nanoparquet.rdx
/usr/lib64/R/library/nanoparquet/help/paths.rds
/usr/lib64/R/library/nanoparquet/html/00Index.html
/usr/lib64/R/library/nanoparquet/html/R.css
/usr/lib64/R/library/nanoparquet/tests/testthat.R
/usr/lib64/R/library/nanoparquet/tests/testthat/_snaps/arrow-schema.md
/usr/lib64/R/library/nanoparquet/tests/testthat/_snaps/parquet-metadata.md
/usr/lib64/R/library/nanoparquet/tests/testthat/_snaps/porcelain.md
/usr/lib64/R/library/nanoparquet/tests/testthat/_snaps/read-parquet.md
/usr/lib64/R/library/nanoparquet/tests/testthat/_snaps/spelling.md
/usr/lib64/R/library/nanoparquet/tests/testthat/_snaps/write-parquet-2.md
/usr/lib64/R/library/nanoparquet/tests/testthat/_snaps/write-parquet.md
/usr/lib64/R/library/nanoparquet/tests/testthat/data/alltypes_plain.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/alltypes_plain.snappy.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/byte_stream_split.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/byte_stream_split_extended.gzip.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/date.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/dbp-int32-missing.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/dbp-int32.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/dbp-int64.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/decimals.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/delta_byte_array.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/delta_length_byte_array.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/duckdb-bug1589.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/enum.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/enum2.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/factor.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/gzip.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/issue10279_delta_encoding.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/map.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/mtcars-arrow.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/nested_lists.snappy.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/parquet_go.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/rle_boolean_encoding.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/timestamp-ms.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/timestamp.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/timetz.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/uuid-arrow.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/v2-missing.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/zstd-v2.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/data/zstd.parquet
/usr/lib64/R/library/nanoparquet/tests/testthat/helper.R
/usr/lib64/R/library/nanoparquet/tests/testthat/test-arrow-schema.R
/usr/lib64/R/library/nanoparquet/tests/testthat/test-parquet-metadata.R
/usr/lib64/R/library/nanoparquet/tests/testthat/test-porcelain.R
/usr/lib64/R/library/nanoparquet/tests/testthat/test-read-parquet.R
/usr/lib64/R/library/nanoparquet/tests/testthat/test-rle.R
/usr/lib64/R/library/nanoparquet/tests/testthat/test-spelling.R
/usr/lib64/R/library/nanoparquet/tests/testthat/test-utils.R
/usr/lib64/R/library/nanoparquet/tests/testthat/test-write-large-files.R
/usr/lib64/R/library/nanoparquet/tests/testthat/test-write-parquet-2.R
/usr/lib64/R/library/nanoparquet/tests/testthat/test-write-parquet.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/nanoparquet/libs/nanoparquet.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-nanoparquet/34774a54e4b286739f317922b31ba5eb3ec9195e
/usr/share/package-licenses/R-nanoparquet/7d3772817ef6dd00f95c6841e07552968eb74600
/usr/share/package-licenses/R-nanoparquet/f39758dda00281db4eefbe95ee61c3cc225c7102