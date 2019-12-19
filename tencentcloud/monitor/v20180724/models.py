# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tencentcloud.common.abstract_model import AbstractModel


class DataPoint(AbstractModel):
    """Monitoring data point

    """

    def __init__(self):
        """
        :param Dimensions: Combination of instance object dimensions
        :type Dimensions: list of Dimension
        :param Timestamps: The array of timestamps indicating at which points in time there is data. Missing timestamps have no data points (i.e., missed)
        :type Timestamps: list of float
        :param Values: The array of monitoring values, which is in one-to-one correspondence to Timestamps
        :type Values: list of float
        """
        self.Dimensions = None
        self.Timestamps = None
        self.Values = None


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        self.Timestamps = params.get("Timestamps")
        self.Values = params.get("Values")


class DescribeBaseMetricsRequest(AbstractModel):
    """DescribeBaseMetrics request structure.

    """

    def __init__(self):
        """
        :param Namespace: Business namespace
        :type Namespace: str
        :param MetricName: Metric name
        :type MetricName: str
        """
        self.Namespace = None
        self.MetricName = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")


class DescribeBaseMetricsResponse(AbstractModel):
    """DescribeBaseMetrics response structure.

    """

    def __init__(self):
        """
        :param MetricSet: Listed of queried metric descriptions
        :type MetricSet: list of MetricSet
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MetricSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MetricSet") is not None:
            self.MetricSet = []
            for item in params.get("MetricSet"):
                obj = MetricSet()
                obj._deserialize(item)
                self.MetricSet.append(obj)
        self.RequestId = params.get("RequestId")


class Dimension(AbstractModel):
    """Combination of instance object dimensions

    """

    def __init__(self):
        """
        :param Name: Instance dimension name
        :type Name: str
        :param Value: Instance dimension value
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class DimensionsDesc(AbstractModel):
    """Dimension information

    """

    def __init__(self):
        """
        :param Dimensions: Array of dimension names
        :type Dimensions: list of str
        """
        self.Dimensions = None


    def _deserialize(self, params):
        self.Dimensions = params.get("Dimensions")


class GetMonitorDataRequest(AbstractModel):
    """GetMonitorData request structure.

    """

    def __init__(self):
        """
        :param Namespace: Namespace. Each Tencent Cloud product has a namespace
        :type Namespace: str
        :param MetricName: Metric name. For detailed metric descriptions of each Tencent Cloud product, see the corresponding [Monitoring API](https://cloud.tencent.com/document/product/248/30384) document
        :type MetricName: str
        :param Instances: Combination of instance object dimensions
        :type Instances: list of Instance
        :param Period: Monitoring statistical period. The default value is 300, and the unit is s
        :type Period: int
        :param StartTime: Start time such as 2018-09-22T19:51:23+08:00
        :type StartTime: str
        :param EndTime: End time. Uses the current time by default and cannot be earlier than StartTime
        :type EndTime: str
        """
        self.Namespace = None
        self.MetricName = None
        self.Instances = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class GetMonitorDataResponse(AbstractModel):
    """GetMonitorData response structure.

    """

    def __init__(self):
        """
        :param Period: Statistical period
        :type Period: int
        :param MetricName: Metric name
        :type MetricName: str
        :param DataPoints: Array of data points
        :type DataPoints: list of DataPoint
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Period = None
        self.MetricName = None
        self.DataPoints = None
        self.StartTime = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.MetricName = params.get("MetricName")
        if params.get("DataPoints") is not None:
            self.DataPoints = []
            for item in params.get("DataPoints"):
                obj = DataPoint()
                obj._deserialize(item)
                self.DataPoints.append(obj)
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """Array of instance dimension combinations

    """

    def __init__(self):
        """
        :param Dimensions: Combination of instance dimensions
        :type Dimensions: list of Dimension
        """
        self.Dimensions = None


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)


class MetricObjectMeaning(AbstractModel):
    """Meaning of metric data

    """

    def __init__(self):
        """
        :param En: Meaning of the metric in English
        :type En: str
        :param Zh: Meaning of the metric in Chinese
        :type Zh: str
        """
        self.En = None
        self.Zh = None


    def _deserialize(self, params):
        self.En = params.get("En")
        self.Zh = params.get("Zh")


class MetricSet(AbstractModel):
    """Description of the unit and supported statistical period of the business metric

    """

    def __init__(self):
        """
        :param Namespace: Namespace. Each Tencent Cloud product has a namespace
        :type Namespace: str
        :param MetricName: Metric Name
        :type MetricName: str
        :param Unit: Unit used by the metric
        :type Unit: str
        :param UnitCname: Unit used by the metric
        :type UnitCname: str
        :param Period: Statistical period in seconds supported by the metric, such as 60 and 300
        :type Period: list of int
        :param Periods: Metric method during the statistical period
        :type Periods: list of PeriodsSt
        :param Meaning: Meaning of the statistical metric
        :type Meaning: :class:`tencentcloud.monitor.v20180724.models.MetricObjectMeaning`
        :param Dimensions: Dimension description
        :type Dimensions: list of DimensionsDesc
        """
        self.Namespace = None
        self.MetricName = None
        self.Unit = None
        self.UnitCname = None
        self.Period = None
        self.Periods = None
        self.Meaning = None
        self.Dimensions = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")
        self.Unit = params.get("Unit")
        self.UnitCname = params.get("UnitCname")
        self.Period = params.get("Period")
        if params.get("Periods") is not None:
            self.Periods = []
            for item in params.get("Periods"):
                obj = PeriodsSt()
                obj._deserialize(item)
                self.Periods.append(obj)
        if params.get("Meaning") is not None:
            self.Meaning = MetricObjectMeaning()
            self.Meaning._deserialize(params.get("Meaning"))
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = DimensionsDesc()
                obj._deserialize(item)
                self.Dimensions.append(obj)


class PeriodsSt(AbstractModel):
    """Statistical method during the period

    """

    def __init__(self):
        """
        :param Period: Period
        :type Period: str
        :param StatType: Statistical method
        :type StatType: list of str
        """
        self.Period = None
        self.StatType = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.StatType = params.get("StatType")